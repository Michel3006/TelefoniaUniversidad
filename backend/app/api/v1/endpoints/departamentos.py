from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.v1.crud import build_crud
from app.db.session import get_db
from app.models.organizacion import Departamento
from app.schemas.organizacion import DepartamentoCreate, DepartamentoRead, DepartamentoUpdate

router = APIRouter(prefix="/departamentos", tags=["departamentos"])


@router.get("/raices", response_model=list[DepartamentoRead])
def raices(db: Session = Depends(get_db)):
    return db.scalars(
        select(Departamento).where(Departamento.departamento_padre_id.is_(None))
    ).all()


build_crud(router, Departamento, DepartamentoCreate, DepartamentoUpdate, DepartamentoRead, entidad="departamentos")


@router.get("/{departamento_id}/subordinados", response_model=list[DepartamentoRead])
def subordinados(departamento_id: int, db: Session = Depends(get_db)):
    depto = db.get(Departamento, departamento_id)
    if depto is None:
        raise HTTPException(status_code=404, detail="No existe el departamento")
    return db.scalars(
        select(Departamento).where(Departamento.departamento_padre_id == departamento_id)
    ).all()
