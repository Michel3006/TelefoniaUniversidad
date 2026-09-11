from datetime import datetime

from pydantic import BaseModel, ConfigDict


class HistorialRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    entidad: str
    entidad_id: int
    accion: str
    campo: str | None = None
    valor_anterior: str | None = None
    valor_nuevo: str | None = None
    usuario_id: int | None = None
    fecha: datetime