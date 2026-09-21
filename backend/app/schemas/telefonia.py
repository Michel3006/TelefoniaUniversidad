import re
from typing import Any

from pydantic import BaseModel, ConfigDict, field_validator


def _no_vacio(v: Any) -> Any:
    if isinstance(v, str) and not v.strip():
        return None
    return v


_PATRON_TELEFONO = r"^[\d\s+()-]{6,30}$"
_PATRON_EXTENSION = r"^\d{1,6}$"
_PATRON_SIM = r"^[\d\s+.-]{6,30}$"
_PATRON_ICCID = r"^\d{15,20}$"
_PATRON_IMSI = r"^\d{15}$"
_PATRON_IMEI = r"^\d{15}$"


class TelefonoBase(BaseModel):
    numero: str
    local_id: int | None = None
    estado_id: int | None = None
    observaciones: str | None = None

    @field_validator("numero")
    @classmethod
    def _validar_numero(cls, v: str) -> str:
        v = v.strip()
        if not re.fullmatch(_PATRON_TELEFONO, v):
            raise ValueError("El numero de telefono tiene un formato invalido")
        return v

    _vaciar_obs = field_validator("observaciones", mode="before")(_no_vacio)


class TelefonoCreate(TelefonoBase):
    pass


class TelefonoUpdate(TelefonoBase):
    pass


class TelefonoRead(TelefonoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class ExtensionBase(BaseModel):
    numero: str
    telefono_id: int | None = None
    estado_id: int | None = None
    observaciones: str | None = None

    @field_validator("numero")
    @classmethod
    def _validar_numero(cls, v: str) -> str:
        v = v.strip()
        if not re.fullmatch(_PATRON_EXTENSION, v):
            raise ValueError("La extension debe tener entre 1 y 6 digitos")
        return v

    _vaciar_obs = field_validator("observaciones", mode="before")(_no_vacio)


class ExtensionCreate(ExtensionBase):
    pass


class ExtensionUpdate(ExtensionBase):
    pass


class ExtensionRead(ExtensionBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class SimBase(BaseModel):
    numero: str
    iccid: str | None = None
    imsi: str | None = None
    operador: str = "ETECSA"
    plan_id: int | None = None
    estado_id: int | None = None

    @field_validator("numero")
    @classmethod
    def _validar_numero(cls, v: str) -> str:
        v = v.strip()
        if not re.fullmatch(_PATRON_SIM, v):
            raise ValueError("El numero de SIM tiene un formato invalido (6-30 caracteres)")
        return v

    @field_validator("iccid")
    @classmethod
    def _validar_iccid(cls, v: str | None) -> str | None:
        v = _no_vacio(v)
        if v is not None and not re.fullmatch(_PATRON_ICCID, v):
            raise ValueError("El ICCID debe tener entre 15 y 20 digitos")
        return v

    @field_validator("imsi")
    @classmethod
    def _validar_imsi(cls, v: str | None) -> str | None:
        v = _no_vacio(v)
        if v is not None and not re.fullmatch(_PATRON_IMSI, v):
            raise ValueError("El IMSI debe tener exactamente 15 digitos")
        return v


class SimCreate(SimBase):
    pass


class SimUpdate(SimBase):
    pass


class SimRead(SimBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class DispositivoBase(BaseModel):
    marca: str
    modelo: str
    imei: str
    sim_id: int | None = None
    local_id: int | None = None
    estado_id: int | None = None
    observaciones: str | None = None

    @field_validator("imei")
    @classmethod
    def _validar_imei(cls, v: str) -> str:
        v = v.strip()
        if not re.fullmatch(_PATRON_IMEI, v):
            raise ValueError("El IMEI debe tener exactamente 15 digitos")
        return v

    _vaciar_obs = field_validator("observaciones", mode="before")(_no_vacio)


class DispositivoCreate(DispositivoBase):
    pass


class DispositivoUpdate(DispositivoBase):
    pass


class DispositivoRead(DispositivoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class ExtensionResumen(BaseModel):
    id: int
    numero: str
    estado: str | None = None
    responsable: str | None = None


class TelefonoDetalle(BaseModel):
    id: int
    numero: str
    local: str | None = None
    edificio: str | None = None
    estado: str | None = None
    observaciones: str | None = None
    extensiones: list[ExtensionResumen] = []


class SimDetalle(BaseModel):
    id: int
    numero: str
    operador: str | None = None
    plan: str | None = None
    iccid: str | None = None
    imsi: str | None = None
    estado: str | None = None
    dispositivo: str | None = None
    responsable: str | None = None
    consumo_ultimo_periodo: float | None = None
    en_exceso_ultimo_periodo: bool | None = None