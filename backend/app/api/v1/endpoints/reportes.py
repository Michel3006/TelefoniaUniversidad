from fastapi import APIRouter, Depends, Query
from sqlalchemy import and_, case, func, select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.asignaciones import Asignacion
from app.models.consumo import Consumo, FacturaEtecsa
from app.models.telefonia import Dispositivo, Extension, Sim, Telefono
from app.models.personas import Persona

router = APIRouter(prefix="/reportes", tags=["reportes"])


@router.get("/inventario")
def inventario(db: Session = Depends(get_db)):
    def contar(modelo):
        return db.scalar(select(func.count()).select_from(modelo))

    return {
        "telefonos_fijos": contar(Telefono),
        "sims": contar(Sim),
        "dispositivos": contar(Dispositivo),
        "personas": contar(Persona),
    }


@router.get("/recursos-por-departamento")
def recursos_por_departamento(db: Session = Depends(get_db)):
    results = db.execute(
        select(
            Persona.departamento_id,
            func.count(func.distinct(Sim.id)).label("sims"),
            func.count(func.distinct(Dispositivo.id)).label("dispositivos"),
        )
        .select_from(Persona)
        .outerjoin(
            Asignacion,
            (Asignacion.persona_id == Persona.id)
            & (Asignacion.fecha_fin.is_(None)),
        )
        .outerjoin(
            Sim,
            (Asignacion.tipo_recurso == "sim")
            & (Asignacion.recurso_id == Sim.id),
        )
        .outerjoin(
            Dispositivo,
            (Asignacion.tipo_recurso == "dispositivo")
            & (Asignacion.recurso_id == Dispositivo.id),
        )
        .group_by(Persona.departamento_id)
    ).all()
    return [
        {"departamento_id": r[0], "sims": r[1], "dispositivos": r[2]}
        for r in results
    ]


@router.get("/consumo-por-periodo")
def consumo_por_periodo(db: Session = Depends(get_db)):
    rows = db.execute(
        select(
            FacturaEtecsa.periodo,
            func.count(Consumo.id).label("registros"),
            func.sum(Consumo.consumo).label("consumo"),
            func.sum(Consumo.importe).label("importe"),
            func.sum(case((Consumo.en_exceso.is_(True), 1), else_=0)).label("excesos"),
            func.sum(
                case(
                    (and_(Consumo.en_exceso.is_(True), Consumo.con_autorizacion.is_(True)), 1),
                    else_=0,
                )
            ).label("excesos_autorizados"),
            func.sum(case((Consumo.sim_id.is_(None), 1), else_=0)).label("no_asociados"),
        )
        .select_from(Consumo)
        .join(FacturaEtecsa, Consumo.factura_id == FacturaEtecsa.id)
        .group_by(FacturaEtecsa.periodo)
        .order_by(FacturaEtecsa.periodo.desc())
    ).all()
    return [
        {
            "periodo": r[0],
            "registros": r[1] or 0,
            "consumo": r[2] or 0,
            "importe": r[3] or 0,
            "excesos": r[4] or 0,
            "excesos_autorizados": r[5] or 0,
            "no_asociados": r[6] or 0,
        }
        for r in rows
    ]


@router.get("/excesos")
def excesos(
    periodo: str | None = Query(None, description="Formato: YYYY-MM"),
    autorizado: bool | None = Query(None),
    db: Session = Depends(get_db),
):
    query = (
        select(Consumo, Sim.numero, FacturaEtecsa.periodo)
        .select_from(Consumo)
        .join(FacturaEtecsa, Consumo.factura_id == FacturaEtecsa.id)
        .outerjoin(Sim, Consumo.sim_id == Sim.id)
        .where(Consumo.en_exceso.is_(True))
    )
    if periodo is not None:
        query = query.where(FacturaEtecsa.periodo == periodo)
    if autorizado is not None:
        query = query.where(Consumo.con_autorizacion.is_(autorizado))
    query = query.order_by(FacturaEtecsa.periodo.desc(), Consumo.consumo.desc())

    return [
        {
            "id": c.id,
            "numero": numero or c.numero_detectado,
            "sim_id": c.sim_id,
            "periodo": periodo_col,
            "consumo": c.consumo,
            "importe": c.importe,
            "limite_normal": c.limite_normal,
            "limite_efectivo": c.limite_efectivo,
            "en_exceso": c.en_exceso,
            "con_autorizacion": c.con_autorizacion,
        }
        for c, numero, periodo_col in db.execute(query).all()
    ]


@router.get("/recursos-sin-asignar")
def recursos_sin_asignar(db: Session = Depends(get_db)):
    activos = db.scalars(select(Asignacion).where(Asignacion.fecha_fin.is_(None))).all()
    ocupados: dict[str, list[int]] = {}
    for a in activos:
        ocupados.setdefault(a.tipo_recurso, []).append(a.recurso_id)

    def _restantes(modelo: type, tipo_recurso: str, etiqueta) -> list[dict]:
        query = select(modelo)
        if ocupados.get(tipo_recurso):
            query = query.where(modelo.id.notin_(ocupados[tipo_recurso]))
        return [
            {"tipo": tipo_recurso, "id": fila.id, "descripcion": etiqueta(fila)}
            for fila in db.scalars(query).all()
        ]

    return {
        "sims": _restantes(Sim, "sim", lambda f: f.numero),
        "dispositivos": _restantes(Dispositivo, "dispositivo", lambda f: f"{f.marca} {f.modelo}"),
        "telefonos": _restantes(Telefono, "telefono", lambda f: f.numero),
        "extensiones": _restantes(Extension, "extension", lambda f: f.numero),
    }


@router.get("/recursos-por-persona")
def recursos_por_persona(db: Session = Depends(get_db)):
    rows = db.execute(
        select(Asignacion, Persona.nombre, Persona.departamento_id)
        .join(Persona, Asignacion.persona_id == Persona.id)
        .where(Asignacion.fecha_fin.is_(None))
        .order_by(Persona.nombre)
    ).all()

    agrupadas: dict[int, dict] = {}
    for a, nombre, depto_id in rows:
        grupo = agrupadas.setdefault(
            a.persona_id,
            {"persona_id": a.persona_id, "nombre": nombre, "departamento_id": depto_id, "recursos": []},
        )
        grupo["recursos"].append(
            {
                "tipo_recurso": a.tipo_recurso,
                "recurso_id": a.recurso_id,
                "fecha_inicio": a.fecha_inicio.isoformat(),
            }
        )
    return list(agrupadas.values())
