from pydantic import BaseModel, ConfigDict


class EstadoBase(BaseModel):
    nombre: str
    descripcion: str | None = None


class EstadoCreate(EstadoBase):
    pass


class EstadoUpdate(EstadoBase):
    pass


class EstadoRead(EstadoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int