from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Date, DateTime, ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class FacturaEtecsa(Base):
    """Cabecera de una factura mensual de ETECSA importada desde PDF."""

    __tablename__ = "facturas_etecsa"

    id: Mapped[int] = mapped_column(primary_key=True)
    no_factura: Mapped[str] = mapped_column(String(40), unique=True, index=True)
    numero_cliente: Mapped[str | None] = mapped_column(String(30))
    folio: Mapped[str | None] = mapped_column(String(30))
    periodo: Mapped[str] = mapped_column(String(7), index=True)  # YYYY-MM
    fecha_factura: Mapped[date | None] = mapped_column(Date)
    fecha_vencimiento: Mapped[date | None] = mapped_column(Date)
    moneda: Mapped[str] = mapped_column(String(10), default="CUP")

    cuota_total: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))
    consumo_total: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))
    comision_total: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))
    impuesto_total: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))
    facturado_total: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))
    atraso: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))
    total_a_pagar: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))
    consumo_voz: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))
    consumo_sms: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))

    archivo_origen: Mapped[str | None] = mapped_column(String(255))
    procesado_en: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    consumos: Mapped[list["Consumo"]] = relationship(back_populates="factura", cascade="all, delete-orphan")


class Consumo(Base):
    """Consumo mensual de una SIM segun una factura de ETECSA. Nunca se
    sobrescribe: cada periodo genera sus propias filas (historico)."""

    __tablename__ = "consumo"

    id: Mapped[int] = mapped_column(primary_key=True)
    factura_id: Mapped[int] = mapped_column(ForeignKey("facturas_etecsa.id"), index=True)
    sim_id: Mapped[int | None] = mapped_column(ForeignKey("sims.id"), index=True)
    numero_detectado: Mapped[str] = mapped_column(String(30), index=True)

    cuota: Mapped[Decimal] = mapped_column(Numeric(14, 2), default=0)
    consumo: Mapped[Decimal] = mapped_column(Numeric(14, 2), default=0)
    comision: Mapped[Decimal] = mapped_column(Numeric(14, 2), default=0)
    impuesto: Mapped[Decimal] = mapped_column(Numeric(14, 2), default=0)
    importe: Mapped[Decimal] = mapped_column(Numeric(14, 2), default=0)

    en_exceso: Mapped[bool] = mapped_column(default=False)
    con_autorizacion: Mapped[bool] = mapped_column(default=False)
    limite_normal: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))
    limite_efectivo: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))

    factura: Mapped[FacturaEtecsa] = relationship(back_populates="consumos")
    sim: Mapped["Sim | None"] = relationship(back_populates="consumos")


class LimiteConsumo(Base):
    """Limite de consumo (importe) autorizado para una SIM. Historico por
    vigencia: al cambiar el limite se cierra vigente_hasta y se crea uno
    nuevo, no se sobrescribe."""

    __tablename__ = "limites_consumo"

    id: Mapped[int] = mapped_column(primary_key=True)
    sim_id: Mapped[int] = mapped_column(ForeignKey("sims.id"), index=True)
    valor_limite: Mapped[Decimal] = mapped_column(Numeric(14, 2))
    vigente_desde: Mapped[date] = mapped_column(Date)
    vigente_hasta: Mapped[date | None] = mapped_column(Date)
    observaciones: Mapped[str | None] = mapped_column(Text)

    sim: Mapped["Sim"] = relationship()


class AutorizacionExceso(Base):
    """Excepcion que permite a una persona/SIM superar el limite normal
    durante un periodo determinado."""

    __tablename__ = "autorizaciones_exceso"

    id: Mapped[int] = mapped_column(primary_key=True)
    sim_id: Mapped[int] = mapped_column(ForeignKey("sims.id"), index=True)
    persona_id: Mapped[int] = mapped_column(ForeignKey("personas.id"), index=True)
    limite_autorizado: Mapped[Decimal] = mapped_column(Numeric(14, 2))
    fecha_inicio: Mapped[date] = mapped_column(Date)
    fecha_fin: Mapped[date | None] = mapped_column(Date)
    motivo: Mapped[str | None] = mapped_column(Text)
    responsable: Mapped[str | None] = mapped_column(String(150))
    observaciones: Mapped[str | None] = mapped_column(Text)

    sim: Mapped["Sim"] = relationship()
    persona: Mapped["Persona"] = relationship()
