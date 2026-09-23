from datetime import date

from pydantic import BaseModel, ConfigDict


class DepartamentoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str
    departamento_padre_id: int | None = None
    id_direccion: str | None = None
    nivel: int | None = None
    id_area: int | None = None
    fecha_alta: date | None = None
    fecha_baja: date | None = None
    baja: bool = False