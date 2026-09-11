from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Coste(Base):
    __tablename__ = "costes"

    id: Mapped[int] = mapped_column(primary_key=True)
    periodo: Mapped[str] = mapped_column(String(7), index=True)  # YYYY-MM
    concepto: Mapped[str] = mapped_column(String(150))
    monto: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    moneda: Mapped[str] = mapped_column(String(10), default="ARS")
    departamento_id: Mapped[int | None] = mapped_column(ForeignKey("departamentos.id"))
    linea_id: Mapped[int | None] = mapped_column(ForeignKey("lineas.id"))
    contrato_id: Mapped[int | None] = mapped_column(ForeignKey("contratos.id"))