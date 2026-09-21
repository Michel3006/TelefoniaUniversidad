from fastapi import APIRouter, Depends, HTTPException, Query, Request, status
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.api.v1.utils import like_seguro
from app.core.security import get_current_user, require_role
from app.db.session import get_db
from app.models.historial import Historial
from app.models.personas import Persona
from app.schemas.personas import PersonaCreate, PersonaRead, PersonaUpdate

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


@router.post(
    "/",
    response_model=PersonaRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_role("admin", "gestor"))],
)
def create_persona(payload: PersonaCreate, request: Request, db: Session = Depends(get_db)):
    persona = Persona(**payload.model_dump())
    db.add(persona)
    db.flush()
    db.add(
        Historial(
            entidad="personas",
            entidad_id=persona.id,
            accion="creado",
            usuario_id=_user_id(request),
        )
    )
    db.commit()
    db.refresh(persona)
    return persona


@router.put(
    "/{persona_id}",
    response_model=PersonaRead,
    dependencies=[Depends(require_role("admin", "gestor"))],
)
def update_persona(
    persona_id: int,
    payload: PersonaUpdate,
    request: Request,
    db: Session = Depends(get_db),
):
    persona = _obtener_o_404(db, persona_id)
    for campo, valor in payload.model_dump(exclude_unset=True).items():
        anterior = getattr(persona, campo)
        setattr(persona, campo, valor)
        if anterior != valor:
            db.add(
                Historial(
                    entidad="personas",
                    entidad_id=persona_id,
                    accion="actualizado",
                    campo=campo,
                    valor_anterior=str(anterior) if anterior is not None else None,
                    valor_nuevo=str(valor) if valor is not None else None,
                    usuario_id=_user_id(request),
                )
            )
    db.commit()
    db.refresh(persona)
    return persona


@router.delete(
    "/{persona_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    dependencies=[Depends(require_role("admin", "gestor"))],
)
def delete_persona(persona_id: int, request: Request, db: Session = Depends(get_db)):
    persona = _obtener_o_404(db, persona_id)
    db.delete(persona)
    db.add(
        Historial(
            entidad="personas",
            entidad_id=persona_id,
            accion="eliminado",
            usuario_id=_user_id(request),
        )
    )
    db.commit()


def _user_id(request: Request) -> int | None:
    user = getattr(request.state, "user", None)
    return user.id if user else None