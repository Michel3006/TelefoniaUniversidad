"""fusion de Linea en Sim: SIM = recurso movil unico (numero + SIM fisica)

No hay datos reales en produccion todavia (confirmado con el cliente), por
lo que esta migracion recrea el modelo sin logica de transformacion de
datos existentes. Si en el futuro se ejecuta sobre una instalacion con
datos, debe revisarse primero.

Revision ID: 004_fusion_sim_linea
Revises: 003_integracion_institucional
Create Date: 2026-09-17
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "004_fusion_sim_linea"
down_revision: Union[str, None] = "003_integracion_institucional"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # dispositivos y costes referenciaban "lineas"; ahora referencian "sims"
    with op.batch_alter_table("dispositivos") as batch_op:
        batch_op.drop_column("linea_id")
        batch_op.add_column(sa.Column("sim_id", sa.Integer(), sa.ForeignKey("sims.id", name="fk_dispositivos_sim_id"), nullable=True))

    with op.batch_alter_table("costes") as batch_op:
        batch_op.drop_column("linea_id")
        batch_op.add_column(sa.Column("sim_id", sa.Integer(), sa.ForeignKey("sims.id", name="fk_costes_sim_id"), nullable=True))

    op.drop_table("lineas")

    # sims: numero propio + iccid/imsi opcionales
    with op.batch_alter_table("sims") as batch_op:
        batch_op.add_column(sa.Column("numero", sa.String(30), nullable=True))
        batch_op.add_column(sa.Column("plan_id", sa.Integer(), sa.ForeignKey("planes.id", name="fk_sims_plan_id"), nullable=True))
        batch_op.alter_column("iccid", existing_type=sa.String(30), nullable=True)
    op.create_index(op.f("ix_sims_numero"), "sims", ["numero"], unique=True)


def downgrade() -> None:
    op.drop_index(op.f("ix_sims_numero"), table_name="sims")
    with op.batch_alter_table("sims") as batch_op:
        batch_op.alter_column("iccid", existing_type=sa.String(30), nullable=False)
        batch_op.drop_column("plan_id")
        batch_op.drop_column("numero")

    op.create_table(
        "lineas",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("numero", sa.String(30), unique=True, index=True),
        sa.Column("operador", sa.String(100), nullable=True, server_default="ETECSA"),
        sa.Column("plan_id", sa.Integer(), sa.ForeignKey("planes.id"), nullable=True),
        sa.Column("sim_id", sa.Integer(), sa.ForeignKey("sims.id"), nullable=True),
        sa.Column("estado_id", sa.Integer(), sa.ForeignKey("estados.id"), nullable=True),
    )

    with op.batch_alter_table("costes") as batch_op:
        batch_op.drop_column("sim_id")
        batch_op.add_column(sa.Column("linea_id", sa.Integer(), sa.ForeignKey("lineas.id", name="fk_costes_linea_id"), nullable=True))

    with op.batch_alter_table("dispositivos") as batch_op:
        batch_op.drop_column("sim_id")
        batch_op.add_column(sa.Column("linea_id", sa.Integer(), sa.ForeignKey("lineas.id", name="fk_dispositivos_linea_id"), nullable=True))
