from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.api.v1.utils import like_seguro
from app.core.security import get_current_user
from app.db.session import get_db
from app.models.personas import Persona

router = APIRouter(prefix="/personas", tags=["personas"])

_CAMPOS_SENSIBLES = ("documento", "email", "telefono", "exttelef")


def _rol_usuario(user) -> str:
    return user.rol.nombre if user and user.rol else ""


def _serializar(persona: Persona, rol: str) -> dict:
    datos = {c.name: getattr(persona, c.name) for c in Persona.__table__.columns}
    if rol == "consulta":
        for campo in _CAMPOS_SENSIBLES:
            datos.pop(campo, None)
    return datos


def _obtener_o_404(db: Session, persona_id: int) -> Persona:
    persona = db.get(Persona, persona_id)
    if persona is None:
        raise HTTPException(status_code=404, detail="No existe la persona")
    return persona


@router.get("/buscar")
def buscar(
    q: str = Query(..., min_length=1, max_length=100),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=50),
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    rol = _rol_usuario(user)
    termino = like_seguro(q)
    condiciones = [
        Persona.nombre.ilike(termino, escape="\\"),
        Persona.apellido.ilike(termino, escape="\\"),
        Persona.apellido_2.ilike(termino, escape="\\"),
        Persona.id_empleado.ilike(termino, escape="\\"),
    ]
    if rol != "consulta":
        condiciones += [
            Persona.email.ilike(termino, escape="\\"),
            Persona.documento.ilike(termino, escape="\\"),
        ]
    filas = db.scalars(
        select(Persona).where(or_(*condiciones)).offset(skip).limit(limit)
    ).all()
    return [_serializar(p, rol) for p in filas]


@router.get("/")
def list_personas(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    rol = _rol_usuario(user)
    filas = db.scalars(select(Persona).offset(skip).limit(limit)).all()
    return [_serializar(p, rol) for p in filas]


@router.get("/{persona_id}")
def get_persona(
    persona_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    rol = _rol_usuario(user)
    return _serializar(_obtener_o_404(db, persona_id), rol)