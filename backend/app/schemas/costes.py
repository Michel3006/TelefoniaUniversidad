import calendar
import re
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator

_PATRON_PERIODO = r"^\d{4}-(0[1-9]|1[0-2])$"


class CosteBase(BaseModel):
    periodo: str  # YYYY-MM
    importe: Decimal
    observaciones: str | None = None
    departamento_id: int | None = None
    sim_id: int | None = None

    @field_validator("periodo")
    @classmethod
    def _validar_periodo(cls, v: str) -> str:
        if not re.fullmatch(_PATRON_PERIODO, v):
            raise ValueError("El periodo debe tener formato YYYY-MM")
        anio, mes = v.split("-")
        calendar.monthrange(int(anio), int(mes))
        return v

    @field_validator("importe")
    @classmethod
    def _validar_importe(cls, v: Decimal) -> Decimal:
        if v <= 0:
            raise ValueError("El importe debe ser mayor que cero")
        return v


class CosteCreate(CosteBase):
    pass


class CosteUpdate(CosteBase):
    pass


class CosteRead(CosteBase):
    model_config = ConfigDict(from_attributes=True)

    id: int