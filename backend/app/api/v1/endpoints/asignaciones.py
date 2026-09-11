from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.asignaciones import Asignacion
from app.models.historial import Historial
from app.schemas.asignaciones import AsignacionCreate, AsignacionRead, AsignacionUpdate

router = APIRouter(prefix="/asignaciones", tags=["asignaciones"])


@router.get("/activas", response_model=list[AsignacionRead])
def activas(db: Session = Depends(get_db)):
    return db.scalars(
        select(Asignacion).where(Asignacion.fecha_fin.is_(None))
    ).all()


@router.get("/por-recurso", response_model=list[AsignacionRead])
def por_recurso(
    tipo_recurso: str,
    recurso_id: int,
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
    return db.scalars(query).all()


@router.get("/por-persona/{persona_id}", response_model=list[AsignacionRead])
def por_persona(persona_id: int, db: Session = Depends(get_db)):
    return db.scalars(
        select(Asignacion).where(Asignacion.persona_id == persona_id)
    ).all()


@router.get("/", response_model=list[AsignacionRead])
def list_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return db.scalars(select(Asignacion).offset(skip).limit(limit)).all()


@router.get("/{asignacion_id}", response_model=AsignacionRead)
def get_item(asignacion_id: int, db: Session = Depends(get_db)):
    item = db.get(Asignacion, asignacion_id)
    if item is None:
        raise HTTPException(status_code=404, detail="No existe la asignacion")
    return item


@router.post("/", response_model=AsignacionRead, status_code=201)
def create_item(payload: AsignacionCreate, db: Session = Depends(get_db)):
    item = Asignacion(**payload.model_dump())
    db.add(item)
    db.flush()
    db.add(Historial(entidad="asignaciones", entidad_id=item.id, accion="creado"))
    db.commit()
    db.refresh(item)
    return item


@router.put("/{asignacion_id}", response_model=AsignacionRead)
def update_item(asignacion_id: int, payload: AsignacionUpdate, db: Session = Depends(get_db)):
    item = db.get(Asignacion, asignacion_id)
    if item is None:
        raise HTTPException(status_code=404, detail="No existe la asignacion")
    for campo, valor in payload.model_dump(exclude_unset=True).items():
        setattr(item, campo, valor)
    db.add(Historial(entidad="asignaciones", entidad_id=asignacion_id, accion="actualizado"))
    db.commit()
    db.refresh(item)
    return item


@router.delete("/{asignacion_id}", status_code=204)
def delete_item(asignacion_id: int, db: Session = Depends(get_db)):
    item = db.get(Asignacion, asignacion_id)
    if item is None:
        raise HTTPException(status_code=404, detail="No existe la asignacion")
    db.delete(item)
    db.add(Historial(entidad="asignaciones", entidad_id=asignacion_id, accion="eliminado"))
    db.commit()


@router.put("/{asignacion_id}/finalizar", response_model=AsignacionRead)
def finalizar(asignacion_id: int, db: Session = Depends(get_db)):
    asignacion = db.get(Asignacion, asignacion_id)
    if asignacion is None:
        raise HTTPException(status_code=404, detail="No existe la asignacion")
    if asignacion.fecha_fin is not None:
        raise HTTPException(status_code=400, detail="La asignacion ya esta finalizada")
    asignacion.fecha_fin = date.today()
    db.commit()
    db.refresh(asignacion)
    return asignacion
