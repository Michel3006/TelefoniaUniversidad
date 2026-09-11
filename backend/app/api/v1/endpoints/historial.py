from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.historial import Historial
from app.schemas.historial import HistorialRead

router = APIRouter(prefix="/historial", tags=["historial"])


@router.get("/", response_model=list[HistorialRead])
def listar(
    entidad: str | None = Query(None),
    entidad_id: int | None = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    query = select(Historial).order_by(Historial.fecha.desc()).offset(skip).limit(limit)
    if entidad:
        query = query.where(Historial.entidad == entidad)
    if entidad_id is not None:
        query = query.where(Historial.entidad_id == entidad_id)
    return db.scalars(query).all()