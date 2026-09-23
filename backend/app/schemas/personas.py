from pydantic import BaseModel, ConfigDict


class PersonaBase(BaseModel):
    nombre: str
    apellido: str
    apellido_2: str | None = None
    documento: str | None = None
    email: str | None = None
    telefono: str | None = None
    exttelef: str | None = None
    departamento_id: int | None = None
    id_empleado: str | None = None
    id_expediente: str | None = None
    id_ccosto: str | None = None
    cargo_id: int | None = None
    area_id: int | None = None
    cubiculo: str | None = None
    direccion: str | None = None
    ciudad: str | None = None
    baja: bool = False


class PersonaCreate(PersonaBase):
    pass


class PersonaUpdate(PersonaBase):
    pass


class PersonaRead(PersonaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class PersonaReadBasico(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str
    apellido: str
    apellido_2: str | None = None
    departamento_id: int | None = None
    id_empleado: str | None = None
    id_expediente: str | None = None
    id_ccosto: str | None = None
    cargo_id: int | None = None
    area_id: int | None = None
    cubiculo: str | None = None
    direccion: str | None = None
    ciudad: str | None = None
    baja: bool = False