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
    db: Session = Depends(get_db),
):
    return db.scalars(
        select(Coste).where(Coste.periodo == periodo)
    ).all()


build_crud(
    router, Coste, CosteCreate, CosteUpdate, CosteRead, entidad="costes",
    write_dependency=Depends(require_role("admin", "gestor")),
)


@router.get("/por-departamento/{departamento_id}", response_model=list[CosteRead])
def por_departamento(departamento_id: int, db: Session = Depends(get_db)):
    return db.scalars(
        select(Coste).where(Coste.departamento_id == departamento_id)
    ).all()


@router.get("/por-sim/{sim_id}", response_model=list[CosteRead])
def por_sim(sim_id: int, db: Session = Depends(get_db)):
    return db.scalars(
        select(Coste).where(Coste.sim_id == sim_id)
    ).all()
