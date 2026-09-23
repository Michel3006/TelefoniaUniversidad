"""eliminar Costos, Planes y Limites: el PDF de ETECSA es la fuente de verdad

Punto 7 del PLAN_CAMBIOS. Se eliminan las tablas `costes`, `planes` y
`limites_consumo`, y la columna `sims.plan_id`. La cuota del PDF reemplaza
al plan/limite manual; el importe se toma directamente del PDF.

Revision ID: 009_eliminar_costes_planes_limites
Revises: 008_eliminar_locales_ubicacion_personas
Create Date: 2026-09-23
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "009_eliminar_costes_planes_limites"
down_revision: Union[str, None] = "008_eliminar_locales_ubicacion_personas"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("sims") as batch:
        batch.drop_column("plan_id")

    op.drop_table("costes")
    op.drop_table("limites_consumo")
    op.drop_table("planes")


def downgrade() -> None:
    op.create_table(
        "planes",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre", sa.String(150), index=True),
        sa.Column("operador", sa.String(100), nullable=True, server_default="ETECSA"),
        sa.Column("contrato_id", sa.Integer(), sa.ForeignKey("contratos.id"), nullable=True),
        sa.Column("coste_mensual", sa.Numeric(12, 2), nullable=True),
        sa.Column("descripcion", sa.Text(), nullable=True),
    )

    op.create_table(
        "costes",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("periodo", sa.String(7), index=True),
        sa.Column("importe", sa.Numeric(12, 2)),
        sa.Column("observaciones", sa.String(150)),
        sa.Column("departamento_id", sa.Integer(), sa.ForeignKey("departamentos.id"), nullable=True),
        sa.Column("sim_id", sa.Integer(), sa.ForeignKey("sims.id"), nullable=True),
    )

    op.create_table(
        "limites_consumo",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("sim_id", sa.Integer(), sa.ForeignKey("sims.id"), nullable=False),
        sa.Column("valor_limite", sa.Numeric(14, 2), nullable=False),
        sa.Column("vigente_desde", sa.Date(), nullable=False),
        sa.Column("vigente_hasta", sa.Date(), nullable=True),
        sa.Column("observaciones", sa.Text(), nullable=True),
    )
    op.create_index(op.f("ix_limites_consumo_sim_id"), "limites_consumo", ["sim_id"], unique=False)

    with op.batch_alter_table("sims") as batch:
        batch.add_column(sa.Column("plan_id", sa.Integer(), sa.ForeignKey("planes.id"), nullable=True))
