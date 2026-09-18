from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.api.v1.crud import build_crud
from app.core.security import require_role
from app.db.session import get_db
from app.models.telefonia import Sim
from app.schemas.telefonia import SimCreate, SimDetalle, SimRead, SimUpdate
from app.services.telefonia import get_sim_detalle

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
                Sim.numero.ilike(termino),
                Sim.iccid.ilike(termino),
                Sim.imsi.ilike(termino),
            )
        )
    ).all()


@router.get("/{sim_id}/detalle", response_model=SimDetalle)
def detalle(sim_id: int, db: Session = Depends(get_db)):
    data = get_sim_detalle(db, sim_id)
    if data is None:
        raise HTTPException(status_code=404, detail="No existe la SIM")
    return data


build_crud(
    router, Sim, SimCreate, SimUpdate, SimRead, entidad="sims",
    write_dependency=Depends(require_role("admin", "gestor")),
)
