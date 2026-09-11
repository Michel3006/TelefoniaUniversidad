"""quitar modulo proveedores

Revision ID: 002_quitar_proveedores
Revises: 001_initial
Create Date: 2026-09-11

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "002_quitar_proveedores"
down_revision: Union[str, None] = "001_initial"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("contratos") as batch_op:
        batch_op.drop_column("proveedor_id")
    op.drop_table("proveedores")


def downgrade() -> None:
    op.create_table(
        "proveedores",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre", sa.String(150), index=True),
        sa.Column("cuit", sa.String(20), unique=True, nullable=True),
        sa.Column("contacto", sa.String(150), nullable=True),
        sa.Column("email", sa.String(150), nullable=True),
        sa.Column("telefono", sa.String(50), nullable=True),
        sa.Column("observaciones", sa.Text(), nullable=True),
    )
    with op.batch_alter_table("contratos") as batch_op:
        batch_op.add_column(sa.Column("proveedor_id", sa.Integer(), sa.ForeignKey("proveedores.id"), nullable=True))