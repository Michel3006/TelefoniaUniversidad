from fastapi import APIRouter

from app.api.v1.crud import build_crud
from app.models.planes import Plan
from app.schemas.planes import PlanCreate, PlanRead, PlanUpdate

router = APIRouter(prefix="/planes", tags=["planes"])

build_crud(router, Plan, PlanCreate, PlanUpdate, PlanRead, entidad="planes")