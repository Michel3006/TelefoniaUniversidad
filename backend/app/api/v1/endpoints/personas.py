from fastapi import APIRouter
from fastapi import Depends, Query
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.api.v1.crud import build_crud
from app.db.session import get_db
from app.models.personas import Persona
from app.schemas.personas import PersonaCreate, PersonaRead, PersonaUpdate

router = APIRouter(prefix="/personas", tags=["personas"])


@router.get("/buscar", response_model=list[PersonaRead])
def buscar(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
):
    termino = f"%{q}%"
    return db.scalars(
        select(Persona).where(
            or_(
                Persona.nombre.ilike(termino),
                Persona.apellido.ilike(termino),
                Persona.email.ilike(termino),
                Persona.documento.ilike(termino),
            )
        )
    ).all()


build_crud(router, Persona, PersonaCreate, PersonaUpdate, PersonaRead, entidad="personas")
