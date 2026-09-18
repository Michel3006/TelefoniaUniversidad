from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.v1.crud import build_crud
from app.core.security import require_role
from app.db.session import get_db
from app.models.telefonia import Extension
from app.schemas.telefonia import ExtensionCreate, ExtensionRead, ExtensionUpdate

router = APIRouter(prefix="/extensiones", tags=["extensiones"])


@router.get("/buscar", response_model=list[ExtensionRead])
def buscar(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
):
    termino = f"%{q}%"
    return db.scalars(
        select(Extension).where(Extension.numero.ilike(termino))
    ).all()


build_crud(
    router, Extension, ExtensionCreate, ExtensionUpdate, ExtensionRead, entidad="extensiones",
    write_dependency=Depends(require_role("admin", "gestor")),
)


@router.get("/por-telefono/{telefono_id}", response_model=list[ExtensionRead])
def por_telefono(telefono_id: int, db: Session = Depends(get_db)):
    return db.scalars(
        select(Extension).where(Extension.telefono_id == telefono_id)
    ).all()
