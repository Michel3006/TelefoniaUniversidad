from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.v1.crud import build_crud
from app.db.session import get_db
from app.models.telefonia import Linea
from app.schemas.telefonia import LineaCreate, LineaDetalle, LineaRead, LineaUpdate
from app.services.telefonia import get_linea_detalle

router = APIRouter(prefix="/lineas", tags=["lineas"])

build_crud(router, Linea, LineaCreate, LineaUpdate, LineaRead, entidad="lineas")


@router.get("/{linea_id}/detalle", response_model=LineaDetalle)
def detalle(linea_id: int, db: Session = Depends(get_db)):
    data = get_linea_detalle(db, linea_id)
    if data is None:
        raise HTTPException(status_code=404, detail="No existe la linea")
    return data