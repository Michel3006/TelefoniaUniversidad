from pydantic import BaseModel, ConfigDict, EmailStr, field_validator

from app.core.security import validar_politica_password


def _validar_password(password: str) -> str:
    validar_politica_password(password)
    return password


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
    email: EmailStr
    password: str
    rol_id: int

    _validar_password = field_validator("password")(_validar_password)


class UsuarioUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    activo: bool | None = None
    rol_id: int | None = None

    @field_validator("password")
    @classmethod
    def _validar_password_opcional(cls, v: str | None) -> str | None:
        if v is None or v == "":
            return v
        _validar_password(v)
        return v


class UsuarioRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str
    activo: bool
    debe_cambiar_password: bool
    rol: RolRead


class CambiarPasswordRequest(BaseModel):
    password_actual: str
    password_nueva: str

    @field_validator("password_nueva")
    @classmethod
    def _validar_password_nueva(cls, v: str) -> str:
        return _validar_password(v)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"