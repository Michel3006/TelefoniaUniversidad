from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from app.core.security import require_role
from app.db.session import get_db
from app.schemas.institucional import SincronizacionResumen, SincronizacionRrhh
from app.services import institucional

router = APIRouter(
    prefix="/sincronizacion",
    tags=["sincronizacion"],
    dependencies=[Depends(require_role("admin"))],
)

_TAMANO_MAXIMO_RH_JSON = 5 * 1024 * 1024


@router.post("/rh-json", response_model=SincronizacionResumen)
def aplicar_json(payload: SincronizacionRrhh, request: Request, db: Session = Depends(get_db)):
    longitud = request.headers.get("content-length")
    if longitud is not None:
        try:
            if int(longitud) > _TAMANO_MAXIMO_RH_JSON:
                raise HTTPException(
                    status_code=413,
                    detail="La sincronizacion excede el tamano maximo permitido",
                )
        except ValueError:
            pass
    return institucional.aplicar(db, payload.model_dump())


@router.post("/rrhh", response_model=SincronizacionResumen)
def sincronizar(db: Session = Depends(get_db)):
    try:
        return institucional.sincronizar_desde_rrhh(db)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc