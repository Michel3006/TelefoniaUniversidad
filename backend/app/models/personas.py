from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

from app.models.institucional import Area, Cargo


class Persona(Base):
    __tablename__ = "personas"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    apellido: Mapped[str] = mapped_column(String(100))
    documento: Mapped[str | None] = mapped_column(String(30))
    email: Mapped[str | None] = mapped_column(String(150))
    telefono: Mapped[str | None] = mapped_column(String(50))
    departamento_id: Mapped[int | None] = mapped_column(ForeignKey("departamentos.id"))

    id_empleado: Mapped[str | None] = mapped_column(String(15), unique=True, index=True)
    id_expediente: Mapped[str | None] = mapped_column(String(15), index=True)
    apellido_2: Mapped[str | None] = mapped_column(String(50))
    exttelef: Mapped[str | None] = mapped_column(String(15))
    id_ccosto: Mapped[str | None] = mapped_column(String(10))
    cargo_id: Mapped[int | None] = mapped_column(ForeignKey("cargos.id"))
    area_id: Mapped[int | None] = mapped_column(ForeignKey("areas.id"))
    cubiculo: Mapped[str | None] = mapped_column(String(50))
    direccion: Mapped[str | None] = mapped_column(String(255))
    ciudad: Mapped[str | None] = mapped_column(String(50))
    baja: Mapped[bool] = mapped_column(Boolean, default=False)

    departamento: Mapped["Departamento | None"] = relationship()
    cargo: Mapped[Cargo | None] = relationship()
    area: Mapped[Area | None] = relationship()