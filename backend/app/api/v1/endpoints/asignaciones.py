import json
from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import require_role
from app.db.session import get_db
from app.models.asignaciones import Asignacion
from app.models.historial import Historial
from app.models.personas import Persona
from app.schemas.asignaciones import AsignacionCreate, AsignacionRead, AsignacionUpdate
from app.services import asignaciones as servicio_asignaciones

router = APIRouter(prefix="/asignaciones", tags=["asignaciones"])
_gestion = [Depends(require_role("admin", "gestor"))]
_solo_admin = [Depends(require_role("admin"))]


@router.get("/activas", response_model=list[AsignacionRead])
def activas(
    skip: int = Query(0, ge=0),
    limit: int = Query(500, ge=1, le=500),
    db: Session = Depends(get_db),
):
    return db.scalars(
        select(Asignacion)
        .where(Asignacion.fecha_fin.is_(None))
        .offset(skip)
        .limit(limit)
    ).all()


@router.get("/por-recurso", response_model=list[AsignacionRead])
def por_recurso(
    tipo_recurso: str,
    recurso_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(500, ge=1, le=500),
    db: Session = Depends(get_db),
):
    query = (
        select(Asignacion)
        .where(
            Asignacion.tipo_recurso == tipo_recurso,
            Asignacion.recurso_id == recurso_id,
        )
        .order_by(Asignacion.fecha_inicio.desc())
    )
    return db.scalars(query.offset(skip).limit(limit)).all()


@router.get("/por-persona/{persona_id}", response_model=list[AsignacionRead])
def por_persona(
    persona_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(500, ge=1, le=500),
    db: Session = Depends(get_db),
):
    return db.scalars(
        select(Asignacion)
        .where(Asignacion.persona_id == persona_id)
        .offset(skip)
        .limit(limit)
    ).all()


@router.get("/", response_model=list[AsignacionRead])
def list_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    return db.scalars(select(Asignacion).offset(skip).limit(limit)).all()


@router.get("/{asignacion_id}", response_model=AsignacionRead)
def get_item(asignacion_id: int, db: Session = Depends(get_db)):
    item = db.get(Asignacion, asignacion_id)
    if item is None:
        raise HTTPException(status_code=404, detail="No existe la asignacion")
    return item


@router.post("/", response_model=AsignacionRead, status_code=201, dependencies=_gestion)
def create_item(
    payload: AsignacionCreate,
    request: Request,
    db: Session = Depends(get_db),
):
    if not servicio_asignaciones.tipo_recurso_valido(payload.tipo_recurso):
        raise HTTPException(status_code=400, detail=f"tipo_recurso invalido: {payload.tipo_recurso}")
    if not servicio_asignaciones.recurso_existe(db, payload.tipo_recurso, payload.recurso_id):
        raise HTTPException(status_code=404, detail="El recurso indicado no existe")
    if db.get(Persona, payload.persona_id) is None:
        raise HTTPException(status_code=404, detail="La persona indicada no existe")
    _validar_fechas(payload.fecha_inicio, payload.fecha_fin)
    if servicio_asignaciones.tiene_asignacion_activa(db, payload.tipo_recurso, payload.recurso_id):
        raise HTTPException(status_code=409, detail="El recurso ya tiene una asignacion activa")

    item = Asignacion(**payload.model_dump())
    db.add(item)
    db.flush()
    db.add(
        Historial(
            entidad="asignaciones",
            entidad_id=item.id,
            accion="creado",
            valor_nuevo=_json_registro(item),
            usuario_id=_usuario_id(request),
        )
    )
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="El recurso ya tiene una asignacion activa")
    db.refresh(item)
    return item


@router.put("/{asignacion_id}", response_model=AsignacionRead, dependencies=_gestion)
def update_item(
    asignacion_id: int,
    payload: AsignacionUpdate,
    request: Request,
    db: Session = Depends(get_db),
):
    item = db.get(Asignacion, asignacion_id)
    if item is None:
        raise HTTPException(status_code=404, detail="No existe la asignacion")

    cambios = payload.model_dump(exclude_unset=True)
    campos_editables = {"observaciones"}
    if not set(cambios).issubset(campos_editables):
        raise HTTPException(
            status_code=400,
            detail="Solo se puede editar observaciones; para cambiar la asignacion finalicela y cree una nueva",
        )

    for campo, valor in cambios.items():
        anterior = getattr(item, campo)
        setattr(item, campo, valor)
        if anterior != valor:
            db.add(
                Historial(
                    entidad="asignaciones",
                    entidad_id=asignacion_id,
                    accion="actualizado",
                    campo=campo,
                    valor_anterior=str(anterior) if anterior is not None else None,
                    valor_nuevo=str(valor) if valor is not None else None,
                    usuario_id=_usuario_id(request),
                )
            )
    db.commit()
    db.refresh(item)
    return item


@router.delete("/{asignacion_id}", status_code=204, dependencies=_solo_admin)
def delete_item(
    asignacion_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    item = db.get(Asignacion, asignacion_id)
    if item is None:
        raise HTTPException(status_code=404, detail="No existe la asignacion")
    db.delete(item)
    db.add(
        Historial(
            entidad="asignaciones",
            entidad_id=asignacion_id,
            accion="eliminado",
            valor_anterior=_json_registro(item),
            usuario_id=_usuario_id(request),
        )
    )
    db.commit()


@router.put("/{asignacion_id}/finalizar", response_model=AsignacionRead, dependencies=_gestion)
def finalizar(
    asignacion_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    asignacion = db.get(Asignacion, asignacion_id)
    if asignacion is None:
        raise HTTPException(status_code=404, detail="No existe la asignacion")
    if asignacion.fecha_fin is not None:
        raise HTTPException(status_code=400, detail="La asignacion ya esta finalizada")
    asignacion.fecha_fin = date.today()
    db.add(
        Historial(
            entidad="asignaciones",
            entidad_id=asignacion_id,
            accion="desasignado",
            valor_anterior=_json_registro(asignacion),
            usuario_id=_usuario_id(request),
        )
    )
    db.commit()
    db.refresh(asignacion)
    return asignacion


def _validar_fechas(fecha_inicio: date, fecha_fin: date | None) -> None:
    if fecha_fin is not None and fecha_fin < fecha_inicio:
        raise HTTPException(status_code=422, detail="fecha_fin debe ser mayor o igual que fecha_inicio")


def _usuario_id(request: Request) -> int | None:
    user = getattr(request.state, "user", None)
    return user.id if user else None


def _json_registro(item: Asignacion) -> str:
    datos = item.__dict__.copy()
    datos.pop("_sa_instance_state", None)
    return json.dumps(datos, default=str, ensure_ascii=False)