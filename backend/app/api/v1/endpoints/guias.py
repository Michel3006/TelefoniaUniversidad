from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.session import get_db
from app.models.asignaciones import Asignacion
from app.models.personas import Persona
from app.models.telefonia import Dispositivo, Extension, Sim, Telefono

router = APIRouter(prefix="/guias", tags=["guias"])

_CAMPOS_SENSIBLES = ("documento", "email", "telefono", "exttelef")


def _rol_usuario(user) -> str:
    return user.rol.nombre if user and user.rol else ""


@router.get("/telefonica")
def guia_telefonica(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    rol = _rol_usuario(user)

    personas = db.scalars(
        select(Persona).order_by(Persona.apellido, Persona.nombre, Persona.apellido_2)
    ).all()

    sims = {s.id: s.numero or s.iccid or f"SIM {s.id}" for s in db.scalars(select(Sim)).all()}
    telefonos = {t.id: t.numero for t in db.scalars(select(Telefono)).all()}
    extensiones = {e.id: e.numero for e in db.scalars(select(Extension)).all()}
    dispositivos = {
        d.id: f"{d.marca} {d.modelo}".strip() for d in db.scalars(select(Dispositivo)).all()
    }

    recursos = {
        "sim": sims,
        "telefono": telefonos,
        "extension": extensiones,
        "dispositivo": dispositivos,
    }

    activas = db.scalars(select(Asignacion).where(Asignacion.fecha_fin.is_(None))).all()
    por_persona: dict[int, list[dict]] = {}
    for a in activas:
        etiqueta = recursos.get(a.tipo_recurso, {}).get(a.recurso_id)
        if etiqueta is None:
            continue
        por_persona.setdefault(a.persona_id, []).append(
            {
                "tipo": a.tipo_recurso,
                "recurso_id": a.recurso_id,
                "etiqueta": etiqueta,
            }
        )

    resultado = []
    for p in personas:
        datos = {
            "persona_id": p.id,
            "nombre": p.nombre,
            "apellido": p.apellido,
            "apellido_2": p.apellido_2,
            "id_empleado": p.id_empleado,
            "cargo": p.cargo.nombre if p.cargo else None,
            "area": p.area.nombre if p.area else None,
            "departamento": p.departamento.nombre if p.departamento else None,
            "cubiculo": p.cubiculo,
            "exttelef": None,
            "telefono": None,
            "documento": None,
            "email": None,
            "recursos": sorted(por_persona.get(p.id, []), key=lambda r: r["etiqueta"]),
        }
        if rol != "consulta":
            datos["exttelef"] = p.exttelef
            datos["telefono"] = p.telefono
            datos["documento"] = p.documento
            datos["email"] = p.email
        resultado.append(datos)

    return resultado