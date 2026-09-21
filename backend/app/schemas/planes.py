from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ContratoBase(BaseModel):
    numero: str
    observaciones: str | None = None
    fecha_inicio: date | None = None
    fecha_vencimiento: date | None = None

    @field_validator("numero")
    @classmethod
    def _numeros(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("numero es obligatorio")
        return v

    @field_validator("fecha_vencimiento")
    @classmethod
    def _vencimiento_no_anterior(cls, v: date | None, info) -> date | None:
        if v is not None and info.data.get("fecha_inicio") is not None:
            if v < info.data["fecha_inicio"]:
                raise ValueError("fecha_vencimiento debe ser mayor o igual que fecha_inicio")
        return v

    @field_validator("observaciones", mode="before")
    @classmethod
    def _vaciar(cls, v):
        if isinstance(v, str) and not v.strip():
            return None
        return v


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
    coste_mensual: Decimal | None = Field(default=None, ge=0)
    descripcion: str | None = None


class PlanCreate(PlanBase):
    pass


class PlanUpdate(PlanBase):
    pass


class PlanRead(PlanBase):
    model_config = ConfigDict(from_attributes=True)

    id: int