from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class CosteBase(BaseModel):
    periodo: str  # YYYY-MM
    concepto: str
    monto: Decimal
    moneda: str = "ARS"
    departamento_id: int | None = None
    linea_id: int | None = None
    contrato_id: int | None = None


class CosteCreate(CosteBase):
    pass


class CosteUpdate(CosteBase):
    pass


class CosteRead(CosteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int