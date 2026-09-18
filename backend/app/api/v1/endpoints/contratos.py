from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.v1.crud import build_crud
from app.core.security import require_role
from app.db.session import get_db
from app.models.planes import Contrato, Plan
from app.schemas.planes import ContratoCreate, ContratoRead, ContratoUpdate, PlanRead

router = APIRouter(prefix="/contratos", tags=["contratos"])

build_crud(
    router, Contrato, ContratoCreate, ContratoUpdate, ContratoRead, entidad="contratos",
    write_dependency=Depends(require_role("admin", "gestor")),
)


@router.get("/{contrato_id}/detalle")
def detalle(contrato_id: int, db: Session = Depends(get_db)):
    contrato = db.get(Contrato, contrato_id)
    if contrato is None:
        raise HTTPException(status_code=404, detail="No existe el contrato")
    planes = db.scalars(
        select(Plan).where(Plan.contrato_id == contrato_id)
    ).all()
    return {
        "id": contrato.id,
        "numero": contrato.numero,
        "observaciones": contrato.observaciones,
        "fecha_inicio": contrato.fecha_inicio,
        "fecha_vencimiento": contrato.fecha_vencimiento,
        "planes": [
            {
                "id": p.id,
                "nombre": p.nombre,
                "operador": p.operador,
                "coste_mensual": p.coste_mensual,
            }
            for p in planes
        ],
    }