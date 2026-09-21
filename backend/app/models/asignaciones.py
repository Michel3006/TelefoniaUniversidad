from datetime import date

from sqlalchemy import Date, ForeignKey, Index, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Asignacion(Base):
    __tablename__ = "asignaciones"

    id: Mapped[int] = mapped_column(primary_key=True)
    persona_id: Mapped[int] = mapped_column(ForeignKey("personas.id"), index=True)
    tipo_recurso: Mapped[str] = mapped_column(String(30), index=True)  # linea | dispositivo | extension | telefono
    recurso_id: Mapped[int] = mapped_column(index=True)
    fecha_inicio: Mapped[date] = mapped_column(Date)
    fecha_fin: Mapped[date | None] = mapped_column(Date)
    observaciones: Mapped[str | None] = mapped_column(Text)

    persona: Mapped["Persona"] = relationship()

    __table_args__ = (
        Index(
            "uq_asignacion_activa",
            "tipo_recurso",
            "recurso_id",
            unique=True,
            postgresql_where=text("fecha_fin IS NULL"),
            sqlite_where=text("fecha_fin IS NULL"),
        ),
    )