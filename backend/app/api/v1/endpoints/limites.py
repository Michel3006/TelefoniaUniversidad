from datetime import date

import json

from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.core.security import require_role
from app.db.session import get_db
from app.models.consumo import LimiteConsumo
from app.models.historial import Historial
from app.schemas.consumo import LimiteConsumoCreate, LimiteConsumoRead, LimiteConsumoUpdate

router = APIRouter(prefix="/limites", tags=["limites"])
_admin = [Depends(require_role("admin"))]


def _existe_solapado(
    db: Session,
    sim_id: int,
    vigente_desde: date,
    vigente_hasta: date | None,
    excluir_id: int | None = None,
) -> bool:
    fin_ref = vigente_hasta or vigente_desde
    consulta = select(LimiteConsumo).where(
        LimiteConsumo.sim_id == sim_id,
        LimiteConsumo.vigente_desde <= fin_ref,
        or_(LimiteConsumo.vigente_hasta.is_(None), LimiteConsumo.vigente_hasta >= vigente_desde),
    )
    if excluir_id is not None:
        consulta = consulta.where(LimiteConsumo.id != excluir_id)
    return db.scalar(consulta) is not None


@router.get("/", response_model=list[LimiteConsumoRead])
def list_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    return db.scalars(select(LimiteConsumo).offset(skip).limit(limit)).all()


@router.get("/{item_id}", response_model=LimiteConsumoRead)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.get(LimiteConsumo, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="No existe el limite")
    return item


@router.post("/", response_model=LimiteConsumoRead, status_code=status.HTTP_201_CREATED, dependencies=_admin)
def create_item(payload: LimiteConsumoCreate, request: Request, db: Session = Depends(get_db)):
    _validar_rango(payload.vigente_desde, payload.vigente_hasta)
    if payload.valor_limite < 0:
        raise HTTPException(status_code=422, detail="valor_limite no puede ser negativo")
    if _existe_solapado(db, payload.sim_id, payload.vigente_desde, payload.vigente_hasta):
        raise HTTPException(status_code=409, detail="El limite se solapa con otro limite de la misma SIM")

    item = LimiteConsumo(**payload.model_dump())
    db.add(item)
    db.flush()
    _historial_creado(db, request, item)
    db.commit()
    db.refresh(item)
    return item


@router.put("/{item_id}", response_model=LimiteConsumoRead, dependencies=_admin)
def update_item(item_id: int, payload: LimiteConsumoUpdate, request: Request, db: Session = Depends(get_db)):
    item = db.get(LimiteConsumo, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="No existe el limite")
    _validar_rango(payload.vigente_desde, payload.vigente_hasta)
    if payload.valor_limite < 0:
        raise HTTPException(status_code=422, detail="valor_limite no puede ser negativo")
    if _existe_solapado(db, payload.sim_id, payload.vigente_desde, payload.vigente_hasta, excluir_id=item_id):
        raise HTTPException(status_code=409, detail="El limite se solapa con otro limite de la misma SIM")

    for campo, valor in payload.model_dump(exclude_unset=True).items():
        anterior = getattr(item, campo)
        setattr(item, campo, valor)
        if anterior != valor:
            db.add(
                Historial(
                    entidad="limites_consumo",
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
    item = db.get(LimiteConsumo, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="No existe el limite")
    db.delete(item)
    db.add(
        Historial(
            entidad="limites_consumo",
            entidad_id=item_id,
            accion="eliminado",
            valor_anterior=_json_registro(item),
            usuario_id=_usuario_id(request),
        )
    )
    db.commit()


def _validar_rango(desde: date, hasta: date | None) -> None:
    if hasta is not None and hasta < desde:
        raise HTTPException(status_code=422, detail="vigente_hasta debe ser mayor o igual que vigente_desde")


def _historial_creado(db: Session, request: Request, item: LimiteConsumo) -> None:
    db.add(
        Historial(
            entidad="limites_consumo",
            entidad_id=item.id,
            accion="creado",
            valor_nuevo=_json_registro(item),
            usuario_id=_usuario_id(request),
        )
    )


def _usuario_id(request: Request) -> int | None:
    user = getattr(request.state, "user", None)
    return user.id if user else None


def _json_registro(item: LimiteConsumo) -> str:
    datos = item.__dict__.copy()
    datos.pop("_sa_instance_state", None)
    return json.dumps(datos, default=str, ensure_ascii=False)