from datetime import datetime

from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import require_role
from app.db.session import get_db
from app.models.auditoria import Auditoria
from app.schemas.auditoria import AuditoriaRead

router = APIRouter(prefix="/auditoria", tags=["auditoria"])


@router.get("/", response_model=list[AuditoriaRead])
def listar(
    metodo: str | None = Query(None, description="GET, POST, PUT, PATCH, DELETE"),
    cargo: str | None = Query(None, description="admin | gestor | consulta"),
    usuario_id: int | None = Query(None),
    estatus: int | None = Query(None),
    desde: datetime | None = Query(None),
    hasta: datetime | None = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
    _admin=Depends(require_role("admin")),
):
    query = select(Auditoria).order_by(Auditoria.fecha.desc()).offset(skip).limit(limit)
    if metodo:
        query = query.where(Auditoria.metodo == metodo.upper())
    if cargo:
        query = query.where(Auditoria.cargo == cargo.lower())
    if usuario_id is not None:
        query = query.where(Auditoria.usuario_id == usuario_id)
    if estatus is not None:
        query = query.where(Auditoria.estatus == estatus)
    if desde is not None:
        query = query.where(Auditoria.fecha >= desde)
    if hasta is not None:
        query = query.where(Auditoria.fecha <= hasta)
    return db.scalars(query).all()


@router.get("/resumen", response_model=dict)
def resumen(db: Session = Depends(get_db), _admin=Depends(require_role("admin"))):
    from sqlalchemy import func

    total = db.scalar(select(func.count()).select_from(Auditoria))
    por_metodo = dict(
        db.execute(select(Auditoria.metodo, func.count()).group_by(Auditoria.metodo)).all()
    )
    por_cargo = dict(
        db.execute(select(Auditoria.cargo, func.count()).group_by(Auditoria.cargo)).all()
    )
    return {"total": total or 0, "por_metodo": por_metodo, "por_cargo": por_cargo}