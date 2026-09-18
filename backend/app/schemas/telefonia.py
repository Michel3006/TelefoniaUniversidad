from pydantic import BaseModel, ConfigDict


class TelefonoBase(BaseModel):
    numero: str
    local_id: int | None = None
    estado_id: int | None = None
    observaciones: str | None = None


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
