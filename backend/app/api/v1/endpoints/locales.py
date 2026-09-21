from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.v1.crud import build_crud
from app.core.security import require_role
from app.db.session import get_db
from app.models.organizacion import Edificio, Local
from app.schemas.organizacion import (
    EdificioCreate,
    EdificioRead,
    EdificioUpdate,
    LocalCreate,
    LocalRead,
    LocalUpdate,
)

edificios_router = APIRouter(prefix="/edificios", tags=["edificios"])
locales_router = APIRouter(prefix="/locales", tags=["locales"])

build_crud(
    edificios_router, Edificio, EdificioCreate, EdificioUpdate, EdificioRead, entidad="edificios",
    write_dependency=Depends(require_role("admin", "gestor")),
)
build_crud(
    locales_router, Local, LocalCreate, LocalUpdate, LocalRead, entidad="locales",
    write_dependency=Depends(require_role("admin", "gestor")),
)


@locales_router.get("/por-edificio/{edificio_id}", response_model=list[LocalRead])
def locales_por_edificio(
    edificio_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(500, ge=1, le=500),
    db: Session = Depends(get_db),
):
    edificio = db.get(Edificio, edificio_id)
    if edificio is None:
        raise HTTPException(status_code=404, detail="No existe el edificio")
    return db.scalars(
        select(Local).where(Local.edificio_id == edificio_id).offset(skip).limit(limit)
    ).all()