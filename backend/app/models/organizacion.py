from datetime import date

from sqlalchemy import Boolean, Date, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from app.models.institucional import Area


class Departamento(Base):
    __tablename__ = "departamentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(150), index=True)
    departamento_padre_id: Mapped[int | None] = mapped_column(ForeignKey("departamentos.id"))

    id_direccion: Mapped[str | None] = mapped_column(String(15), unique=True, index=True)
    nivel: Mapped[int | None] = mapped_column(Integer)
    id_area: Mapped[int | None] = mapped_column(ForeignKey("areas.id"))
    fecha_alta: Mapped[date | None] = mapped_column(Date)
    fecha_baja: Mapped[date | None] = mapped_column(Date)
    baja: Mapped[bool] = mapped_column(Boolean, default=False)

    padre: Mapped["Departamento | None"] = relationship(remote_side=[id], back_populates="hijos")
    hijos: Mapped[list["Departamento"]] = relationship(back_populates="padre")
    area: Mapped[Area | None] = relationship()