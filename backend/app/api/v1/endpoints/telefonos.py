from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.v1.crud import build_crud
from app.core.security import require_role
from app.db.session import get_db
from app.models.telefonia import Telefono
from app.schemas.telefonia import TelefonoCreate, TelefonoDetalle, TelefonoRead, TelefonoUpdate
from app.services.telefonia import get_telefono_detalle

router = APIRouter(prefix="/telefonos", tags=["telefonos"])


@router.get("/buscar", response_model=list[TelefonoRead])
def buscar(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
):
    termino = f"%{q}%"
    return db.scalars(
        select(Telefono).where(Telefono.numero.ilike(termino))
    ).all()


build_crud(
    router, Telefono, TelefonoCreate, TelefonoUpdate, TelefonoRead, entidad="telefonos",
    write_dependency=Depends(require_role("admin", "gestor")),
)


@router.get("/{telefono_id}/detalle", response_model=TelefonoDetalle)
def detalle(telefono_id: int, db: Session = Depends(get_db)):
    data = get_telefono_detalle(db, telefono_id)
    if data is None:
        raise HTTPException(status_code=404, detail="No existe el telefono")
    return data