from fastapi import APIRouter, Depends

from app.api.v1.crud import build_crud
from app.core.security import require_role
from app.models.consumo import LimiteConsumo
from app.schemas.consumo import LimiteConsumoCreate, LimiteConsumoRead, LimiteConsumoUpdate

router = APIRouter(prefix="/limites", tags=["limites"])

build_crud(
    router, LimiteConsumo, LimiteConsumoCreate, LimiteConsumoUpdate, LimiteConsumoRead,
    entidad="limites_consumo",
    write_dependency=Depends(require_role("admin")),
)
