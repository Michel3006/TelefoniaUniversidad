from fastapi import APIRouter, Depends

from app.api.v1.crud import build_crud
from app.core.security import require_role
from app.models.consumo import AutorizacionExceso
from app.schemas.consumo import (
    AutorizacionExcesoCreate,
    AutorizacionExcesoRead,
    AutorizacionExcesoUpdate,
)

router = APIRouter(prefix="/autorizaciones", tags=["autorizaciones"])

build_crud(
    router, AutorizacionExceso, AutorizacionExcesoCreate, AutorizacionExcesoUpdate, AutorizacionExcesoRead,
    entidad="autorizaciones_exceso",
    write_dependency=Depends(require_role("admin")),
)
