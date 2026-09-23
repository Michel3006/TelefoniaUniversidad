from fastapi import APIRouter, Depends
from app.api.v1.crud import build_crud
from app.core.security import require_role
from app.models.planes import Contrato
from app.schemas.planes import ContratoCreate, ContratoRead, ContratoUpdate

router = APIRouter(prefix="/contratos", tags=["contratos"])

build_crud(
    router, Contrato, ContratoCreate, ContratoUpdate, ContratoRead, entidad="contratos",
    write_dependency=Depends(require_role("admin", "gestor")),
)
