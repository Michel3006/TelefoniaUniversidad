from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.asignaciones import Asignacion
from app.models.organizacion import Local
from app.models.personas import Persona
from app.models.telefonia import Dispositivo, Extension, Linea, Telefono


def get_responsable_id(db: Session, tipo_recurso: str, recurso_id: int) -> int | None:
    return db.scalar(
        select(Asignacion.persona_id)
        .where(
            Asignacion.tipo_recurso == tipo_recurso,
            Asignacion.recurso_id == recurso_id,
            Asignacion.fecha_fin.is_(None),
        )
        .order_by(Asignacion.fecha_inicio.desc())
        .limit(1)
    )


def persona_nombre(db: Session, persona_id: int | None) -> str | None:
    if persona_id is None:
        return None
    persona = db.get(Persona, persona_id)
    if persona is None:
        return None
    return f"{persona.nombre} {persona.apellido}"


def get_telefono_detalle(db: Session, telefono_id: int) -> dict | None:
    telefono = db.get(Telefono, telefono_id)
    if telefono is None:
        return None

    extensiones = []
    for ext in db.scalars(
        select(Extension).where(Extension.telefono_id == telefono_id)
    ).all():
        responsables = persona_nombre(db, get_responsable_id(db, "extension", ext.id))
        extensiones.append(
            {
                "id": ext.id,
                "numero": ext.numero,
                "estado": ext.estado.nombre if ext.estado else None,
                "responsable": responsables,
            }
        )

    local_nombre = None
    edificio_nombre = None
    if telefono.local:
        local_nombre = telefono.local.descripcion or (
            f"Piso {telefono.local.piso} - {telefono.local.oficina}" if telefono.local.piso or telefono.local.oficina else None
        )
        edificio_nombre = telefono.local.edificio.nombre if telefono.local.edificio else None

    return {
        "id": telefono.id,
        "numero": telefono.numero,
        "local": local_nombre,
        "edificio": edificio_nombre,
        "estado": telefono.estado.nombre if telefono.estado else None,
        "observaciones": telefono.observaciones,
        "extensiones": extensiones,
    }


def get_linea_detalle(db: Session, linea_id: int) -> dict | None:
    linea = db.get(Linea, linea_id)
    if linea is None:
        return None

    dispositivo = db.scalar(select(Dispositivo).where(Dispositivo.linea_id == linea_id))

    return {
        "id": linea.id,
        "numero": linea.numero,
        "operador": linea.operador.nombre if linea.operador else None,
        "plan": linea.plan.nombre if linea.plan else None,
        "sim_iccid": linea.sim.iccid if linea.sim else None,
        "sim_imsi": linea.sim.imsi if linea.sim else None,
        "estado": linea.estado.nombre if linea.estado else None,
        "dispositivo": f"{dispositivo.marca} {dispositivo.modelo}" if dispositivo else None,
        "responsable": persona_nombre(db, get_responsable_id(db, "linea", linea_id)),
    }