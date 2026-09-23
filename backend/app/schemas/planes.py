from datetime import date

from pydantic import BaseModel, ConfigDict, field_validator


def _no_vacio(v):
    if isinstance(v, str) and not v.strip():
        return None
    return v


class ContratoBase(BaseModel):
    numero: str
    observaciones: str | None = None
    fecha_inicio: date | None = None
    fecha_vencimiento: date | None = None

    _vaciar_obs = field_validator("observaciones", mode="before")(_no_vacio)


class ContratoCreate(ContratoBase):
    pass


class ContratoUpdate(ContratoBase):
    pass


class ContratoRead(ContratoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
