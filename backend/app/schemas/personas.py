from pydantic import BaseModel, ConfigDict


class PersonaBase(BaseModel):
    nombre: str
    apellido: str
    documento: str | None = None
    email: str | None = None
    telefono: str | None = None
    departamento_id: int | None = None


class PersonaCreate(PersonaBase):
    pass


class PersonaUpdate(PersonaBase):
    pass


class PersonaRead(PersonaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int