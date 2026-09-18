from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class FacturaEtecsaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    no_factura: str
    numero_cliente: str | None = None
    folio: str | None = None
    periodo: str
    fecha_factura: date | None = None
    fecha_vencimiento: date | None = None
    moneda: str
    cuota_total: Decimal | None = None
    consumo_total: Decimal | None = None
    comision_total: Decimal | None = None
    impuesto_total: Decimal | None = None
    facturado_total: Decimal | None = None
    atraso: Decimal | None = None
    total_a_pagar: Decimal | None = None
    consumo_voz: Decimal | None = None
    consumo_sms: Decimal | None = None
    procesado_en: datetime


class ConsumoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    factura_id: int
    sim_id: int | None = None
    numero_detectado: str
    cuota: Decimal
    consumo: Decimal
    comision: Decimal
    impuesto: Decimal
    importe: Decimal
    en_exceso: bool
    con_autorizacion: bool
    limite_normal: Decimal | None = None
    limite_efectivo: Decimal | None = None


class ImportacionResumen(BaseModel):
    factura_id: int
    no_factura: str
    periodo: str
    procesados: int
    asociados: int
    no_asociados: int
    excesos: int
    numeros_no_asociados: list[str] = []


class LimiteConsumoBase(BaseModel):
    sim_id: int
    valor_limite: Decimal
    vigente_desde: date
    vigente_hasta: date | None = None
    observaciones: str | None = None


class LimiteConsumoCreate(LimiteConsumoBase):
    pass


class LimiteConsumoUpdate(LimiteConsumoBase):
    pass


class LimiteConsumoRead(LimiteConsumoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class AutorizacionExcesoBase(BaseModel):
    sim_id: int
    persona_id: int
    limite_autorizado: Decimal
    fecha_inicio: date
    fecha_fin: date | None = None
    motivo: str | None = None
    responsable: str | None = None
    observaciones: str | None = None


class AutorizacionExcesoCreate(AutorizacionExcesoBase):
    pass


class AutorizacionExcesoUpdate(AutorizacionExcesoBase):
    pass


class AutorizacionExcesoRead(AutorizacionExcesoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
