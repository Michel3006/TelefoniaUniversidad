from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.asignaciones import Asignacion
from app.models.costes import Coste
from app.models.telefonia import Dispositivo, Linea, Telefono
from app.models.organizacion import Edificio, Local
from app.models.personas import Persona
from app.services import costes as servicio_costes

router = APIRouter(prefix="/reportes", tags=["reportes"])


@router.get("/inventario")
def inventario(db: Session = Depends(get_db)):
    def contar(modelo):
        return db.scalar(select(func.count()).select_from(modelo))

    return {
        "telefonos_fijos": contar(Telefono),
        "lineas_moviles": contar(Linea),
        "dispositivos": contar(Dispositivo),
        "edificios": contar(Edificio),
        "locales": contar(Local),
        "personas": contar(Persona),
    }


@router.get("/costes-totales")
def costes_totales(db: Session = Depends(get_db)):
    return {
        "monto_total": db.scalar(select(func.sum(Coste.monto))),
        "periodos": db.scalar(select(func.count(func.distinct(Coste.periodo)))),
    }


@router.get("/costes-por-departamento")
def costes_por_departamento(db: Session = Depends(get_db)):
    return servicio_costes.resumen_por_departamento(db)


@router.get("/costes-por-operador")
def costes_por_operador(db: Session = Depends(get_db)):
    results = db.execute(
        select(
            Linea.operador_id,
            func.sum(Coste.monto).label("total"),
            func.count(Coste.id).label("cantidad"),
        )
        .join(Coste, Coste.linea_id == Linea.id)
        .group_by(Linea.operador_id)
    ).all()
    return [
        {"operador_id": r[0], "total": r[1], "cantidad": r[2]}
        for r in results
    ]


@router.get("/costes-por-periodo")
def costes_por_periodo(db: Session = Depends(get_db)):
    return servicio_costes.resumen_por_periodo(db)


@router.get("/recursos-por-departamento")
def recursos_por_departamento(db: Session = Depends(get_db)):
    results = db.execute(
        select(
            Persona.departamento_id,
            func.count(func.distinct(Linea.id)).label("lineas"),
            func.count(func.distinct(Dispositivo.id)).label("dispositivos"),
        )
        .select_from(Persona)
        .outerjoin(
            Asignacion,
            (Asignacion.persona_id == Persona.id)
            & (Asignacion.fecha_fin.is_(None)),
        )
        .outerjoin(
            Linea,
            (Asignacion.tipo_recurso == "linea")
            & (Asignacion.recurso_id == Linea.id),
        )
        .outerjoin(
            Dispositivo,
            (Asignacion.tipo_recurso == "dispositivo")
            & (Asignacion.recurso_id == Dispositivo.id),
        )
        .group_by(Persona.departamento_id)
    ).all()
    return [
        {"departamento_id": r[0], "lineas": r[1], "dispositivos": r[2]}
        for r in results
    ]
