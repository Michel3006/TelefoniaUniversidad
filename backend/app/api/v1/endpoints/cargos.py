from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.institucional import Cargo
from app.schemas.institucional import CargoRead

router = APIRouter(prefix="/cargos", tags=["cargos"])


@router.get("/", response_model=list[CargoRead])
def list_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return db.scalars(
        select(Cargo).order_by(Cargo.nombre).offset(skip).limit(limit)
    ).all()


@router.get("/{cargo_id}", response_model=CargoRead)
def get_item(cargo_id: int, db: Session = Depends(get_db)):
    cargo = db.get(Cargo, cargo_id)
    if cargo is None:
        raise HTTPException(status_code=404, detail="No existe el cargo")
    return cargo