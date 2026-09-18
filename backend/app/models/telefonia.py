from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Telefono(Base):
    __tablename__ = "telefonos"

    id: Mapped[int] = mapped_column(primary_key=True)
    numero: Mapped[str] = mapped_column(String(30), unique=True, index=True)
    local_id: Mapped[int | None] = mapped_column(ForeignKey("locales.id"))
    estado_id: Mapped[int | None] = mapped_column(ForeignKey("estados.id"))
    observaciones: Mapped[str | None] = mapped_column(Text)

    local: Mapped["Local | None"] = relationship()
    estado: Mapped["Estado | None"] = relationship()
    extensiones: Mapped[list["Extension"]] = relationship(back_populates="telefono")


class Extension(Base):
    __tablename__ = "extensiones"

    id: Mapped[int] = mapped_column(primary_key=True)
    numero: Mapped[str] = mapped_column(String(30), index=True)
    telefono_id: Mapped[int | None] = mapped_column(ForeignKey("telefonos.id"))
    estado_id: Mapped[int | None] = mapped_column(ForeignKey("estados.id"))
    observaciones: Mapped[str | None] = mapped_column(Text)

    telefono: Mapped[Telefono | None] = relationship(back_populates="extensiones")
    estado: Mapped["Estado | None"] = relationship()


class Sim(Base):
    """Recurso movil institucional: numero + SIM fisica (fusion de las
    antiguas entidades Linea/Sim). ICCID e IMSI son opcionales porque no
    siempre se conocen al dar de alta el recurso."""

    __tablename__ = "sims"

    id: Mapped[int] = mapped_column(primary_key=True)
    numero: Mapped[str] = mapped_column(String(30), unique=True, index=True)
    iccid: Mapped[str | None] = mapped_column(String(30), unique=True)
    imsi: Mapped[str | None] = mapped_column(String(30))
    operador: Mapped[str] = mapped_column(String(100), default="ETECSA")
    plan_id: Mapped[int | None] = mapped_column(ForeignKey("planes.id"))
    estado_id: Mapped[int | None] = mapped_column(ForeignKey("estados.id"))

    plan: Mapped["Plan | None"] = relationship(back_populates="sims")
    estado: Mapped["Estado | None"] = relationship()
    dispositivos: Mapped[list["Dispositivo"]] = relationship(back_populates="sim")
    consumos: Mapped[list["Consumo"]] = relationship(back_populates="sim")


class Dispositivo(Base):
    __tablename__ = "dispositivos"

    id: Mapped[int] = mapped_column(primary_key=True)
    marca: Mapped[str] = mapped_column(String(100))
    modelo: Mapped[str] = mapped_column(String(100))
    imei: Mapped[str] = mapped_column(String(30), unique=True)
    sim_id: Mapped[int | None] = mapped_column(ForeignKey("sims.id"))
    local_id: Mapped[int | None] = mapped_column(ForeignKey("locales.id"))
    estado_id: Mapped[int | None] = mapped_column(ForeignKey("estados.id"))
    observaciones: Mapped[str | None] = mapped_column(Text)

    sim: Mapped[Sim | None] = relationship(back_populates="dispositivos")
    local: Mapped["Local | None"] = relationship()
    estado: Mapped["Estado | None"] = relationship()
