from typing import Any

import json

from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.db.session import get_db
from app.models.historial import Historial


def _seg(valor: Any) -> str | None:
    if valor is None:
        return None
    return str(valor)


def _usuario_id(request: Request) -> int | None:
    user = getattr(request.state, "user", None)
    return user.id if user else None


def build_crud(
    router: APIRouter,
    model: type,
    create_schema: type[BaseModel],
    update_schema: type[BaseModel],
    read_schema: type[BaseModel],
    entidad: str | None = None,
    write_dependency: Any = None,
) -> None:
    """Registra el CRUD generico sobre `router`.

    `write_dependency` (opcional), si se pasa, es un `Depends(...)` que se
    exige SOLO en create/update/delete (permite que la lectura quede
    disponible para roles de consulta mientras la escritura requiere
    admin/gestor).
    """
    write_deps = [write_dependency] if write_dependency is not None else []

    @router.get("/", response_model=list[read_schema])
    def list_items(
        skip: int = Query(0, ge=0),
        limit: int = Query(100, ge=1, le=500),
        db: Session = Depends(get_db),
    ):
        return db.scalars(select(model).offset(skip).limit(limit)).all()

    @router.get("/{item_id}", response_model=read_schema)
    def get_item(item_id: int, db: Session = Depends(get_db)):
        item = db.get(model, item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="No existe el recurso")
        return item

    @router.post("/", response_model=read_schema, status_code=status.HTTP_201_CREATED, dependencies=write_deps)
    def create_item(
        payload: create_schema,
        request: Request,
        db: Session = Depends(get_db),
    ):
        item = model(**payload.model_dump())
        db.add(item)
        db.flush()
        if entidad:
            db.add(
                Historial(
                    entidad=entidad,
                    entidad_id=item.id,
                    accion="creado",
                    valor_nuevo=_json_registro(item),
                    usuario_id=_usuario_id(request),
                )
            )
        db.commit()
        db.refresh(item)
        return item

    @router.put("/{item_id}", response_model=read_schema, dependencies=write_deps)
    def update_item(
        item_id: int,
        payload: update_schema,
        request: Request,
        db: Session = Depends(get_db),
    ):
        item = db.get(model, item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="No existe el recurso")
        for campo, valor in payload.model_dump(exclude_unset=True).items():
            anterior = getattr(item, campo)
            setattr(item, campo, valor)
            if entidad and anterior != valor:
                db.add(
                    Historial(
                        entidad=entidad,
                        entidad_id=item_id,
                        accion="actualizado",
                        campo=campo,
                        valor_anterior=_seg(anterior),
                        valor_nuevo=_seg(valor),
                        usuario_id=_usuario_id(request),
                    )
                )
        db.commit()
        db.refresh(item)
        return item

    @router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=write_deps)
    def delete_item(
        item_id: int,
        request: Request,
        db: Session = Depends(get_db),
    ):
        item = db.get(model, item_id)
        if item is None:
            raise HTTPException(status_code=404, detail="No existe el recurso")
        copia = _json_registro(item)
        db.delete(item)
        if entidad:
            db.add(
                Historial(
                    entidad=entidad,
                    entidad_id=item_id,
                    accion="eliminado",
                    valor_anterior=copia,
                    usuario_id=_usuario_id(request),
                )
            )
        db.commit()


def _json_registro(item: Any) -> str | None:
    """Serializa un registro a JSON (con valores que el schema conoce)."""
    try:
        datos = item.__dict__.copy()
        datos.pop("_sa_instance_state", None)
        return json.dumps(datos, default=str, ensure_ascii=False)
    except (TypeError, AttributeError):
        return None