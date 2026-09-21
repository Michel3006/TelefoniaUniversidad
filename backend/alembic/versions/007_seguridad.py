"""seguridad: politica de contrasenas, cambio obligatorio, bloqueo de
asignaciones activas duplicadas y auditoria de fechas de password

Revision ID: 007_seguridad
Revises: 006_mejoras_consumo_observaciones
Create Date: 2026-09-20
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "007_seguridad"
down_revision: Union[str, None] = "006_mejoras_consumo_observaciones"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # A2/C1: fuerza el cambio de password inicial y registra el momento del ultimo cambio
    # (se usa para invalidar tokens emitidos antes con el claim iat del JWT).
    op.add_column(
        "usuarios",
        sa.Column("debe_cambiar_password", sa.Boolean(), nullable=False, server_default=sa.text("false")),
    )
    op.add_column(
        "usuarios",
        sa.Column("password_changed_at", sa.DateTime(timezone=True), nullable=True),
    )

    # M1: indice unico parcial para evitar dos asignaciones activas del mismo recurso.
    with op.batch_alter_table("asignaciones") as batch:
        batch.create_index(
            "uq_asignacion_activa",
            ["tipo_recurso", "recurso_id"],
            unique=True,
            postgresql_where=sa.text("fecha_fin IS NULL"),
            sqlite_where=sa.text("fecha_fin IS NULL"),
        )


def downgrade() -> None:
    with op.batch_alter_table("asignaciones") as batch:
        batch.drop_index("uq_asignacion_activa")

    op.drop_column("usuarios", "password_changed_at")
    op.drop_column("usuarios", "debe_cambiar_password")