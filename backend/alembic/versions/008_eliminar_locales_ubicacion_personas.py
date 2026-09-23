"""eliminar edificios y locales; ubicacion de personas desde ASSETS_RH

Revision ID: 008_eliminar_locales_ubicacion_personas
Revises: 007_seguridad
Create Date: 2026-09-23
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "008_eliminar_locales_ubicacion_personas"
down_revision: Union[str, None] = "007_seguridad"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # P1: la ubicacion fisica de centros de trabajo no existe en la BD institucional
    # como locales/edificios, se eliminan. Las personas quedan con su cubículo.
    with op.batch_alter_table("telefonos") as batch:
        batch.drop_column("local_id")

    with op.batch_alter_table("dispositivos") as batch:
        batch.drop_column("local_id")

    op.drop_table("locales")
    op.drop_table("edificios")

    op.add_column(
        "personas",
        sa.Column("cubiculo", sa.String(length=50), nullable=True),
    )
    op.add_column(
        "personas",
        sa.Column("direccion", sa.String(length=255), nullable=True),
    )
    op.add_column(
        "personas",
        sa.Column("ciudad", sa.String(length=50), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("personas", "ciudad")
    op.drop_column("personas", "direccion")
    op.drop_column("personas", "cubiculo")

    op.create_table(
        "edificios",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre", sa.String(length=150), nullable=False),
        sa.Column("direccion", sa.String(length=250), nullable=True),
    )
    op.create_table(
        "locales",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("edificio_id", sa.Integer(), sa.ForeignKey("edificios.id"), nullable=False),
        sa.Column("piso", sa.String(length=50), nullable=True),
        sa.Column("oficina", sa.String(length=50), nullable=True),
        sa.Column("descripcion", sa.String(length=250), nullable=True),
    )

    with op.batch_alter_table("dispositivos") as batch:
        batch.add_column(sa.Column("local_id", sa.Integer(), sa.ForeignKey("locales.id"), nullable=True))

    with op.batch_alter_table("telefonos") as batch:
        batch.add_column(sa.Column("local_id", sa.Integer(), sa.ForeignKey("locales.id"), nullable=True))