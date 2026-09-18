from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.asignaciones import Asignacion


def _model_map():
    # import diferido para evitar ciclos; es el UNICO lugar del sistema
    # donde se define la lista de tipos de recurso validos.
    from app.models.telefonia import Dispositivo, Extension, Sim, Telefono

    return {
        "sim": Sim,
        "dispositivo": Dispositivo,
        "extension": Extension,
        "telefono": Telefono,
    }


TIPOS_RECURSO = ("sim", "dispositivo", "extension", "telefono")


def tipo_recurso_valido(tipo_recurso: str) -> bool:
    return tipo_recurso in _model_map()


def recurso_existe(db: Session, tipo_recurso: str, recurso_id: int) -> bool:
    model = _model_map().get(tipo_recurso)
    if model is None:
        return False
    return db.get(model, recurso_id) is not None


def tiene_asignacion_activa(
    db: Session,
    tipo_recurso: str,
    recurso_id: int,
) -> bool:
    return db.scalar(
        select(Asignacion).where(
            Asignacion.tipo_recurso == tipo_recurso,
            Asignacion.recurso_id == recurso_id,
            Asignacion.fecha_fin.is_(None),
        )
    ) is not None


def persona_tiene_asignacion_activa(
    db: Session,
    persona_id: int,
    tipo_recurso: str,
    recurso_id: int,
) -> bool:
    return db.scalar(
        select(Asignacion).where(
            Asignacion.persona_id == persona_id,
            Asignacion.tipo_recurso == tipo_recurso,
            Asignacion.recurso_id == recurso_id,
            Asignacion.fecha_fin.is_(None),
        )
    ) is not None


def obtener_asignacion_activa(
    db: Session,
    tipo_recurso: str,
    recurso_id: int,
) -> Asignacion | None:
    return db.scalar(
        select(Asignacion).where(
            Asignacion.tipo_recurso == tipo_recurso,
            Asignacion.recurso_id == recurso_id,
            Asignacion.fecha_fin.is_(None),
        )
        .order_by(Asignacion.fecha_inicio.desc())
        .limit(1)
    )


def recursos_disponibles(
    db: Session,
    tipo_recurso: str,
    exclude_ids: list[int] | None = None,
) -> list[int]:
    subquery = (
        select(Asignacion.recurso_id)
        .where(
            Asignacion.tipo_recurso == tipo_recurso,
            Asignacion.fecha_fin.is_(None),
        )
    )
    if exclude_ids:
        subquery = subquery.where(Asignacion.recurso_id.notin_(exclude_ids))

    model = _model_map().get(tipo_recurso)
    if model is None:
        return []

    all_ids = db.scalars(select(model.id)).all()
    assigned_ids = db.scalars(subquery).all()
    return [rid for rid in all_ids if rid not in assigned_ids]
