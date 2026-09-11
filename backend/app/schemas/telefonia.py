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
    iccid: str
    imsi: str | None = None
    operador_id: int | None = None
    estado_id: int | None = None


class SimCreate(SimBase):
    pass


class SimUpdate(SimBase):
    pass


class SimRead(SimBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class LineaBase(BaseModel):
    numero: str
    operador_id: int | None = None
    plan_id: int | None = None
    sim_id: int | None = None
    estado_id: int | None = None


class LineaCreate(LineaBase):
    pass


class LineaUpdate(LineaBase):
    pass


class LineaRead(LineaBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class DispositivoBase(BaseModel):
    marca: str
    modelo: str
    imei: str
    linea_id: int | None = None
    local_id: int | None = None
    estado_id: int | None = None


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


class LineaDetalle(BaseModel):
    id: int
    numero: str
    operador: str | None = None
    plan: str | None = None
    sim_iccid: str | None = None
    sim_imsi: str | None = None
    estado: str | None = None
    dispositivo: str | None = None
    responsable: str | None = None