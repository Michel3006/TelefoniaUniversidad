from datetime import date
from decimal import Decimal

from sqlalchemy import Date, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Contrato(Base):
    __tablename__ = "contratos"

    id: Mapped[int] = mapped_column(primary_key=True)
    numero: Mapped[str] = mapped_column(String(50), index=True)
    descripcion: Mapped[str | None] = mapped_column(Text)
    fecha_inicio: Mapped[date | None] = mapped_column(Date)
    fecha_vencimiento: Mapped[date | None] = mapped_column(Date)

    planes: Mapped[list["Plan"]] = relationship(back_populates="contrato")


class Plan(Base):
    __tablename__ = "planes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(150), index=True)
    operador_id: Mapped[int | None] = mapped_column(ForeignKey("operadores.id"))
    contrato_id: Mapped[int | None] = mapped_column(ForeignKey("contratos.id"))
    coste_mensual: Mapped[Decimal | None] = mapped_column(Numeric(12, 2))
    descripcion: Mapped[str | None] = mapped_column(Text)

    operador: Mapped["Operador | None"] = relationship()
    contrato: Mapped[Contrato | None] = relationship(back_populates="planes")
    lineas: Mapped[list["Linea"]] = relationship(back_populates="plan")