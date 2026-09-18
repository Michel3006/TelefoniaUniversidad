from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class ContratoBase(BaseModel):
    numero: str
    observaciones: str | None = None
    fecha_inicio: date | None = None
    fecha_vencimiento: date | None = None


class ContratoCreate(ContratoBase):
    pass


class ContratoUpdate(ContratoBase):
    pass


class ContratoRead(ContratoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class PlanBase(BaseModel):
    nombre: str
    operador: str = "ETECSA"
    contrato_id: int | None = None
    coste_mensual: Decimal | None = None
    descripcion: str | None = None


class PlanCreate(PlanBase):
    pass


class PlanUpdate(PlanBase):
    pass


class PlanRead(PlanBase):
    model_config = ConfigDict(from_attributes=True)

    id: int