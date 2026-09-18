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


class EdificioCreate(BaseModel):
    nombre: str
    direccion: str | None = None


class EdificioUpdate(EdificioCreate):
    pass


class EdificioRead(EdificioCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int


class LocalBase(BaseModel):
    edificio_id: int
    piso: str | None = None
    oficina: str | None = None
    descripcion: str | None = None


class LocalCreate(LocalBase):
    pass


class LocalUpdate(LocalBase):
    pass


class LocalRead(LocalBase):
    model_config = ConfigDict(from_attributes=True)

    id: int