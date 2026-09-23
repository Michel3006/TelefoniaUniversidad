from datetime import date

from sqlalchemy import Date, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Contrato(Base):
    __tablename__ = "contratos"

    id: Mapped[int] = mapped_column(primary_key=True)
    numero: Mapped[str] = mapped_column(String(50), index=True)
    observaciones: Mapped[str | None] = mapped_column(Text)
    fecha_inicio: Mapped[date | None] = mapped_column(Date)
    fecha_vencimiento: Mapped[date | None] = mapped_column(Date)
