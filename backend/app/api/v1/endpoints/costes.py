from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.v1.crud import build_crud
from app.core.security import require_role
from app.db.session import get_db
from app.models.costes import Coste
from app.schemas.costes import CosteCreate, CosteRead, CosteUpdate

router = APIRouter(prefix="/costes", tags=["costes"])


@router.get("/por-periodo", response_model=list[CosteRead])
def por_periodo(
    periodo: str = Query(..., description="Formato: YYYY-MM"),
    skip: int = Query(0, ge=0),
    limit: int = Query(500, ge=1, le=500),
    db: Session = Depends(get_db),
):
    return db.scalars(
        select(Coste).where(Coste.periodo == periodo).offset(skip).limit(limit)
    ).all()


build_crud(
    router, Coste, CosteCreate, CosteUpdate, CosteRead, entidad="costes",
    write_dependency=Depends(require_role("admin", "gestor")),
)


@router.get("/por-departamento/{departamento_id}", response_model=list[CosteRead])
def por_departamento(
    departamento_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(500, ge=1, le=500),
    db: Session = Depends(get_db),
):
    return db.scalars(
        select(Coste).where(Coste.departamento_id == departamento_id).offset(skip).limit(limit)
    ).all()


@router.get("/por-sim/{sim_id}", response_model=list[CosteRead])
def por_sim(
    sim_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(500, ge=1, le=500),
    db: Session = Depends(get_db),
):
    return db.scalars(
        select(Coste).where(Coste.sim_id == sim_id).offset(skip).limit(limit)
    ).all()
