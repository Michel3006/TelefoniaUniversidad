from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.crud import build_crud
from app.db.session import get_db
from app.models.telefonia import Telefono
from app.schemas.telefonia import TelefonoCreate, TelefonoDetalle, TelefonoRead, TelefonoUpdate
from app.services.telefonia import get_telefono_detalle

router = APIRouter(prefix="/telefonos", tags=["telefonos"])

build_crud(router, Telefono, TelefonoCreate, TelefonoUpdate, TelefonoRead, entidad="telefonos")


@router.get("/{telefono_id}/detalle", response_model=TelefonoDetalle)
def detalle(telefono_id: int, db: Session = Depends(get_db)):
    data = get_telefono_detalle(db, telefono_id)
    if data is None:
        raise HTTPException(status_code=404, detail="No existe el telefono")
    return data