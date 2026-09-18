from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Coste(Base):
    __tablename__ = "costes"

    id: Mapped[int] = mapped_column(primary_key=True)
    periodo: Mapped[str] = mapped_column(String(7), index=True)  # YYYY-MM
    importe: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    observaciones: Mapped[str | None] = mapped_column(Text)
    departamento_id: Mapped[int | None] = mapped_column(ForeignKey("departamentos.id"))
    sim_id: Mapped[int | None] = mapped_column(ForeignKey("sims.id"))