from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.v1.crud import build_crud
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

build_crud(edificios_router, Edificio, EdificioCreate, EdificioUpdate, EdificioRead, entidad="edificios")
build_crud(locales_router, Local, LocalCreate, LocalUpdate, LocalRead, entidad="locales")


@locales_router.get("/por-edificio/{edificio_id}", response_model=list[LocalRead])
def locales_por_edificio(edificio_id: int, db: Session = Depends(get_db)):
    edificio = db.get(Edificio, edificio_id)
    if edificio is None:
        raise HTTPException(status_code=404, detail="No existe el edificio")
    return db.scalars(
        select(Local).where(Local.edificio_id == edificio_id)
    ).all()