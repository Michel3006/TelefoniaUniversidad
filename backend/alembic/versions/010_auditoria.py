"""crear tabla auditoria (punto 3: modulo de auditoria completo)

Revision ID: 010_auditoria
Revises: 009_eliminar_costes_planes_limites
Create Date: 2026-09-23
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "010_auditoria"
down_revision: Union[str, None] = "009_eliminar_costes_planes_limites"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "auditoria",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "fecha",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "usuario_id",
            sa.Integer(),
            sa.ForeignKey("usuarios.id", ondelete="SET NULL"),
            nullable=True,
        ),
        sa.Column("usuario_nombre", sa.String(length=80), nullable=True),
        sa.Column("cargo", sa.String(length=50), nullable=True),
        sa.Column("metodo", sa.String(length=10), nullable=False),
        sa.Column("ruta", sa.String(length=255), nullable=False),
        sa.Column("estatus", sa.Integer(), nullable=False),
        sa.Column("ip", sa.String(length=45), nullable=True),
        sa.Column("detalle", sa.Text(), nullable=True),
    )
    op.create_index(op.f("ix_auditoria_estatus"), "auditoria", ["estatus"])
    op.create_index(op.f("ix_auditoria_fecha"), "auditoria", ["fecha"])
    op.create_index(op.f("ix_auditoria_metodo"), "auditoria", ["metodo"])
    op.create_index(op.f("ix_auditoria_usuario_id"), "auditoria", ["usuario_id"])


def downgrade() -> None:
    op.drop_index(op.f("ix_auditoria_usuario_id"), table_name="auditoria")
    op.drop_index(op.f("ix_auditoria_metodo"), table_name="auditoria")
    op.drop_index(op.f("ix_auditoria_fecha"), table_name="auditoria")
    op.drop_index(op.f("ix_auditoria_estatus"), table_name="auditoria")
    op.drop_table("auditoria")