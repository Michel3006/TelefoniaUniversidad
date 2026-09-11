from pydantic import BaseModel, ConfigDict


class DepartamentoBase(BaseModel):
    nombre: str
    departamento_padre_id: int | None = None


class DepartamentoCreate(DepartamentoBase):
    pass


class DepartamentoUpdate(DepartamentoBase):
    pass


class DepartamentoRead(DepartamentoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


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