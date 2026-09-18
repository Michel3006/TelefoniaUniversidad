from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class CosteBase(BaseModel):
    periodo: str  # YYYY-MM
    importe: Decimal
    observaciones: str | None = None
    departamento_id: int | None = None
    sim_id: int | None = None


class CosteCreate(CosteBase):
    pass


class CosteUpdate(CosteBase):
    pass


class CosteRead(CosteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int