from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.v1.crud import build_crud
from app.db.session import get_db
from app.models.planes import Contrato, Plan
from app.schemas.planes import ContratoCreate, ContratoRead, ContratoUpdate, PlanRead

router = APIRouter(prefix="/contratos", tags=["contratos"])

build_crud(router, Contrato, ContratoCreate, ContratoUpdate, ContratoRead, entidad="contratos")


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
        "descripcion": contrato.descripcion,
        "fecha_inicio": contrato.fecha_inicio,
        "fecha_vencimiento": contrato.fecha_vencimiento,
        "planes": [
            {
                "id": p.id,
                "nombre": p.nombre,
                "operador": p.operador.nombre if p.operador else None,
                "coste_mensual": p.coste_mensual,
            }
            for p in planes
        ],
    }