from pydantic import BaseModel, ConfigDict


class RolBase(BaseModel):
    nombre: str
    descripcion: str | None = None


class RolCreate(RolBase):
    pass


class RolUpdate(RolBase):
    pass


class RolRead(RolBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class UsuarioCreate(BaseModel):
    username: str
    email: str
    password: str
    rol_id: int


class UsuarioUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    password: str | None = None
    activo: bool | None = None
    rol_id: int | None = None


class UsuarioRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str
    activo: bool
    rol: RolRead


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"