from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.organizacion import Departamento
from app.schemas.organizacion import DepartamentoRead

router = APIRouter(prefix="/departamentos", tags=["departamentos"])


@router.get("/raices", response_model=list[DepartamentoRead])
def raices(
    skip: int = Query(0, ge=0),
    limit: int = Query(500, ge=1, le=500),
    db: Session = Depends(get_db),
):
    return db.scalars(
        select(Departamento)
        .where(Departamento.departamento_padre_id.is_(None))
        .offset(skip)
        .limit(limit)
    ).all()


@router.get("/", response_model=list[DepartamentoRead])
def list_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    return db.scalars(select(Departamento).offset(skip).limit(limit)).all()


@router.get("/{departamento_id}", response_model=DepartamentoRead)
def get_item(departamento_id: int, db: Session = Depends(get_db)):
    depto = db.get(Departamento, departamento_id)
    if depto is None:
        raise HTTPException(status_code=404, detail="No existe el departamento")
    return depto


@router.get("/{departamento_id}/subordinados", response_model=list[DepartamentoRead])
def subordinados(
    departamento_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(500, ge=1, le=500),
    db: Session = Depends(get_db),
):
    depto = db.get(Departamento, departamento_id)
    if depto is None:
        raise HTTPException(status_code=404, detail="No existe el departamento")
    return db.scalars(
        select(Departamento)
        .where(Departamento.departamento_padre_id == departamento_id)
        .offset(skip)
        .limit(limit)
    ).all()