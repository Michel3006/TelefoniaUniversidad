from datetime import date

from pydantic import BaseModel, ConfigDict


class AsignacionBase(BaseModel):
    persona_id: int
    tipo_recurso: str  # linea | dispositivo | extension | telefono
    recurso_id: int
    fecha_inicio: date
    fecha_fin: date | None = None
    observaciones: str | None = None


class AsignacionCreate(AsignacionBase):
    pass


class AsignacionUpdate(AsignacionBase):
    pass


class AsignacionRead(AsignacionBase):
    model_config = ConfigDict(from_attributes=True)

    id: int