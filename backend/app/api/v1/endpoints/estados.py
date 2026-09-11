from fastapi import APIRouter

from app.api.v1.crud import build_crud
from app.models.catalogos import Estado
from app.schemas.catalogos import EstadoCreate, EstadoRead, EstadoUpdate

router = APIRouter(prefix="/estados", tags=["estados"])

build_crud(router, Estado, EstadoCreate, EstadoUpdate, EstadoRead, entidad="estados")