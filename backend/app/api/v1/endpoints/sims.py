from fastapi import APIRouter, Depends, Query
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.api.v1.crud import build_crud
from app.db.session import get_db
from app.models.telefonia import Sim
from app.schemas.telefonia import SimCreate, SimRead, SimUpdate

router = APIRouter(prefix="/sims", tags=["sims"])


@router.get("/buscar", response_model=list[SimRead])
def buscar(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
):
    termino = f"%{q}%"
    return db.scalars(
        select(Sim).where(
            or_(
                Sim.iccid.ilike(termino),
                Sim.imsi.ilike(termino),
            )
        )
    ).all()


build_crud(router, Sim, SimCreate, SimUpdate, SimRead, entidad="sims")
