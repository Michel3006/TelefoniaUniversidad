from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.institucional import Area
from app.schemas.institucional import AreaRead

router = APIRouter(prefix="/areas", tags=["areas"])


@router.get("/", response_model=list[AreaRead])
def list_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return db.scalars(
        select(Area).order_by(Area.nombre).offset(skip).limit(limit)
    ).all()


@router.get("/{area_id}", response_model=AreaRead)
def get_item(area_id: int, db: Session = Depends(get_db)):
    area = db.get(Area, area_id)
    if area is None:
        raise HTTPException(status_code=404, detail="No existe el area")
    return area