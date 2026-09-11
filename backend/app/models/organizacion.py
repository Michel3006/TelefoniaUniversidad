from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Departamento(Base):
    __tablename__ = "departamentos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(150), index=True)
    departamento_padre_id: Mapped[int | None] = mapped_column(ForeignKey("departamentos.id"))

    padre: Mapped["Departamento | None"] = relationship(remote_side=[id], back_populates="hijos")
    hijos: Mapped[list["Departamento"]] = relationship(back_populates="padre")


class Edificio(Base):
    __tablename__ = "edificios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(150), index=True)
    direccion: Mapped[str | None] = mapped_column(String(250))


class Local(Base):
    __tablename__ = "locales"

    id: Mapped[int] = mapped_column(primary_key=True)
    edificio_id: Mapped[int] = mapped_column(ForeignKey("edificios.id"))
    piso: Mapped[str | None] = mapped_column(String(50))
    oficina: Mapped[str | None] = mapped_column(String(50))
    descripcion: Mapped[str | None] = mapped_column(String(250))

    edificio: Mapped[Edificio] = relationship()