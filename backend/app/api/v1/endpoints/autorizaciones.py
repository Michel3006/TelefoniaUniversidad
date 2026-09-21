from datetime import date

import json

from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.core.security import require_role
from app.db.session import get_db
from app.models.consumo import AutorizacionExceso
from app.models.historial import Historial
from app.schemas.consumo import (
    AutorizacionExcesoCreate,
    AutorizacionExcesoRead,
    AutorizacionExcesoUpdate,
)

router = APIRouter(prefix="/autorizaciones", tags=["autorizaciones"])
_admin = [Depends(require_role("admin"))]


def _existe_solapado(
    db: Session,
    sim_id: int,
    fecha_inicio: date,
    fecha_fin: date | None,
    persona_id: int,
    excluir_id: int | None = None,
) -> bool:
    fin_ref = fecha_fin or fecha_inicio
    consulta = select(AutorizacionExceso).where(
        AutorizacionExceso.sim_id == sim_id,
        AutorizacionExceso.fecha_inicio <= fin_ref,
        or_(AutorizacionExceso.fecha_fin.is_(None), AutorizacionExceso.fecha_fin >= fecha_inicio),
    )
    if excluir_id is not None:
        consulta = consulta.where(AutorizacionExceso.id != excluir_id)
    return db.scalar(consulta) is not None


@router.get("/", response_model=list[AutorizacionExcesoRead])
def list_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    return db.scalars(select(AutorizacionExceso).offset(skip).limit(limit)).all()


@router.get("/{item_id}", response_model=AutorizacionExcesoRead)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.get(AutorizacionExceso, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="No existe la autorizacion")
    return item


@router.post(
    "/",
    response_model=AutorizacionExcesoRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=_admin,
)
def create_item(payload: AutorizacionExcesoCreate, request: Request, db: Session = Depends(get_db)):
    _validar(payload.fecha_inicio, payload.fecha_fin, payload.limite_autorizado)
    if _existe_solapado(db, payload.sim_id, payload.fecha_inicio, payload.fecha_fin, payload.persona_id):
        raise HTTPException(status_code=409, detail="La autorizacion se solapa con otra de la misma SIM")

    item = AutorizacionExceso(**payload.model_dump())
    db.add(item)
    db.flush()
    db.add(
        Historial(
            entidad="autorizaciones_exceso",
            entidad_id=item.id,
            accion="creado",
            valor_nuevo=_json_registro(item),
            usuario_id=_usuario_id(request),
        )
    )
    db.commit()
    db.refresh(item)
    return item


@router.put("/{item_id}", response_model=AutorizacionExcesoRead, dependencies=_admin)
def update_item(item_id: int, payload: AutorizacionExcesoUpdate, request: Request, db: Session = Depends(get_db)):
    item = db.get(AutorizacionExceso, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="No existe la autorizacion")
    _validar(payload.fecha_inicio, payload.fecha_fin, payload.limite_autorizado)
    if _existe_solapado(db, payload.sim_id, payload.fecha_inicio, payload.fecha_fin, payload.persona_id, excluir_id=item_id):
        raise HTTPException(status_code=409, detail="La autorizacion se solapa con otra de la misma SIM")

    for campo, valor in payload.model_dump(exclude_unset=True).items():
        anterior = getattr(item, campo)
        setattr(item, campo, valor)
        if anterior != valor:
            db.add(
                Historial(
                    entidad="autorizaciones_exceso",
                    entidad_id=item_id,
                    accion="actualizado",
                    campo=campo,
                    valor_anterior=str(anterior) if anterior is not None else None,
                    valor_nuevo=str(valor) if valor is not None else None,
                    usuario_id=_usuario_id(request),
                )
            )
    db.commit()
    db.refresh(item)
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=_admin)
def delete_item(item_id: int, request: Request, db: Session = Depends(get_db)):
    item = db.get(AutorizacionExceso, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="No existe la autorizacion")
    db.delete(item)
    db.add(
        Historial(
            entidad="autorizaciones_exceso",
            entidad_id=item_id,
            accion="eliminado",
            valor_anterior=_json_registro(item),
            usuario_id=_usuario_id(request),
        )
    )
    db.commit()


def _validar(fecha_inicio: date, fecha_fin: date | None, limite: float) -> None:
    if fecha_fin is not None and fecha_fin < fecha_inicio:
        raise HTTPException(status_code=422, detail="fecha_fin debe ser mayor o igual que fecha_inicio")
    if limite <= 0:
        raise HTTPException(status_code=422, detail="limite_autorizado debe ser mayor que cero")


def _usuario_id(request: Request) -> int | None:
    user = getattr(request.state, "user", None)
    return user.id if user else None


def _json_registro(item: AutorizacionExceso) -> str:
    datos = item.__dict__.copy()
    datos.pop("_sa_instance_state", None)
    return json.dumps(datos, default=str, ensure_ascii=False)