from fastapi import APIRouter

from app.api.v1.crud import build_crud
from app.models.catalogos import Operador
from app.schemas.catalogos import OperadorCreate, OperadorRead, OperadorUpdate

router = APIRouter(prefix="/operadores", tags=["operadores"])

build_crud(router, Operador, OperadorCreate, OperadorUpdate, OperadorRead, entidad="operadores")