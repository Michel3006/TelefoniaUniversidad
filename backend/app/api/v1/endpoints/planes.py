from fastapi import APIRouter, Depends

from app.api.v1.crud import build_crud
from app.core.security import require_role
from app.models.planes import Plan
from app.schemas.planes import PlanCreate, PlanRead, PlanUpdate

router = APIRouter(prefix="/planes", tags=["planes"])

build_crud(
    router, Plan, PlanCreate, PlanUpdate, PlanRead, entidad="planes",
    write_dependency=Depends(require_role("admin", "gestor")),
)