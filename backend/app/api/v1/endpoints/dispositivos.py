from fastapi import APIRouter, Depends, Query
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.api.v1.crud import build_crud
from app.core.security import require_role
from app.db.session import get_db
from app.models.telefonia import Dispositivo
from app.schemas.telefonia import DispositivoCreate, DispositivoRead, DispositivoUpdate

router = APIRouter(prefix="/dispositivos", tags=["dispositivos"])


@router.get("/buscar", response_model=list[DispositivoRead])
def buscar(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
):
    termino = f"%{q}%"
    return db.scalars(
        select(Dispositivo).where(
            or_(
                Dispositivo.marca.ilike(termino),
                Dispositivo.modelo.ilike(termino),
                Dispositivo.imei.ilike(termino),
            )
        )
    ).all()


build_crud(
    router, Dispositivo, DispositivoCreate, DispositivoUpdate, DispositivoRead, entidad="dispositivos",
    write_dependency=Depends(require_role("admin", "gestor")),
)
