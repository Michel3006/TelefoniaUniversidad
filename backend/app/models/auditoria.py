from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Auditoria(Base):
    """Registro de auditoría de todas las operaciones del sistema.

    A diferencia del Historial (que conserva el detalle por campo de una
    entidad), la auditoría guarda la operación HTTP completa: quién la hizo
    (usuario + cargo), cuándo (fecha/hora completa), con qué método, contra
    qué recurso, con qué detalle exacto (payload enmascarado), el estatus de
    la respuesta y la IP de origen. El panel es exclusivo del rol admin.
    """

    __tablename__ = "auditoria"

    id: Mapped[int] = mapped_column(primary_key=True)
    fecha: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), index=True
    )
    usuario_id: Mapped[int | None] = mapped_column(
        ForeignKey("usuarios.id", ondelete="SET NULL"), index=True
    )
    # Instantáneas al momento de la operación: el registro se conserva legible
    # aunque el usuario cambie de rol, se edite o se elimine (nombre/cargo).
    usuario_nombre: Mapped[str | None] = mapped_column(String(80))
    cargo: Mapped[str | None] = mapped_column(String(50))
    metodo: Mapped[str] = mapped_column(String(10), index=True)
    ruta: Mapped[str] = mapped_column(String(255))
    estatus: Mapped[int] = mapped_column(Integer, index=True)
    ip: Mapped[str | None] = mapped_column(String(45))
    detalle: Mapped[str | None] = mapped_column(Text)
