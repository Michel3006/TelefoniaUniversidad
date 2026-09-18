"""mejoras de consumo y auditoria: limite normal/efectivo, autorizacion
vigente en el consumo, observaciones de dispositivo

Revision ID: 006_mejoras_consumo_observaciones
Revises: 005_consumo_limites_autorizaciones
Create Date: 2026-09-19
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "006_mejoras_consumo_observaciones"
down_revision: Union[str, None] = "005_consumo_limites_autorizaciones"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("dispositivos", sa.Column("observaciones", sa.Text(), nullable=True))

    op.add_column("consumo", sa.Column("con_autorizacion", sa.Boolean(), nullable=False, server_default=sa.text("false")))
    op.add_column("consumo", sa.Column("limite_normal", sa.Numeric(14, 2), nullable=True))
    op.add_column("consumo", sa.Column("limite_efectivo", sa.Numeric(14, 2), nullable=True))


def downgrade() -> None:
    op.drop_column("consumo", "limite_efectivo")
    op.drop_column("consumo", "limite_normal")
    op.drop_column("consumo", "con_autorizacion")

    op.drop_column("dispositivos", "observaciones")