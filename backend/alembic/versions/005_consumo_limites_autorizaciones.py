"""modulo de consumo ETECSA: facturas, consumo historico, limites y
autorizaciones especiales de exceso

Revision ID: 005_consumo_limites_autorizaciones
Revises: 004_fusion_sim_linea
Create Date: 2026-09-17
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "005_consumo_limites_autorizaciones"
down_revision: Union[str, None] = "004_fusion_sim_linea"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "facturas_etecsa",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("no_factura", sa.String(40), nullable=False),
        sa.Column("numero_cliente", sa.String(30), nullable=True),
        sa.Column("folio", sa.String(30), nullable=True),
        sa.Column("periodo", sa.String(7), nullable=False),
        sa.Column("fecha_factura", sa.Date(), nullable=True),
        sa.Column("fecha_vencimiento", sa.Date(), nullable=True),
        sa.Column("moneda", sa.String(10), nullable=False, server_default="CUP"),
        sa.Column("cuota_total", sa.Numeric(14, 2), nullable=True),
        sa.Column("consumo_total", sa.Numeric(14, 2), nullable=True),
        sa.Column("comision_total", sa.Numeric(14, 2), nullable=True),
        sa.Column("impuesto_total", sa.Numeric(14, 2), nullable=True),
        sa.Column("facturado_total", sa.Numeric(14, 2), nullable=True),
        sa.Column("atraso", sa.Numeric(14, 2), nullable=True),
        sa.Column("total_a_pagar", sa.Numeric(14, 2), nullable=True),
        sa.Column("consumo_voz", sa.Numeric(14, 2), nullable=True),
        sa.Column("consumo_sms", sa.Numeric(14, 2), nullable=True),
        sa.Column("archivo_origen", sa.String(255), nullable=True),
        sa.Column("procesado_en", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )
    op.create_index(op.f("ix_facturas_etecsa_no_factura"), "facturas_etecsa", ["no_factura"], unique=True)
    op.create_index(op.f("ix_facturas_etecsa_periodo"), "facturas_etecsa", ["periodo"], unique=False)

    op.create_table(
        "consumo",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("factura_id", sa.Integer(), sa.ForeignKey("facturas_etecsa.id"), nullable=False),
        sa.Column("sim_id", sa.Integer(), sa.ForeignKey("sims.id"), nullable=True),
        sa.Column("numero_detectado", sa.String(30), nullable=False),
        sa.Column("cuota", sa.Numeric(14, 2), nullable=False, server_default="0"),
        sa.Column("consumo", sa.Numeric(14, 2), nullable=False, server_default="0"),
        sa.Column("comision", sa.Numeric(14, 2), nullable=False, server_default="0"),
        sa.Column("impuesto", sa.Numeric(14, 2), nullable=False, server_default="0"),
        sa.Column("importe", sa.Numeric(14, 2), nullable=False, server_default="0"),
        sa.Column("en_exceso", sa.Boolean(), nullable=False, server_default=sa.text("false")),
    )
    op.create_index(op.f("ix_consumo_factura_id"), "consumo", ["factura_id"], unique=False)
    op.create_index(op.f("ix_consumo_sim_id"), "consumo", ["sim_id"], unique=False)
    op.create_index(op.f("ix_consumo_numero_detectado"), "consumo", ["numero_detectado"], unique=False)

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

    op.create_table(
        "autorizaciones_exceso",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("sim_id", sa.Integer(), sa.ForeignKey("sims.id"), nullable=False),
        sa.Column("persona_id", sa.Integer(), sa.ForeignKey("personas.id"), nullable=False),
        sa.Column("limite_autorizado", sa.Numeric(14, 2), nullable=False),
        sa.Column("fecha_inicio", sa.Date(), nullable=False),
        sa.Column("fecha_fin", sa.Date(), nullable=True),
        sa.Column("motivo", sa.Text(), nullable=True),
        sa.Column("responsable", sa.String(150), nullable=True),
        sa.Column("observaciones", sa.Text(), nullable=True),
    )
    op.create_index(op.f("ix_autorizaciones_exceso_sim_id"), "autorizaciones_exceso", ["sim_id"], unique=False)
    op.create_index(op.f("ix_autorizaciones_exceso_persona_id"), "autorizaciones_exceso", ["persona_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_autorizaciones_exceso_persona_id"), table_name="autorizaciones_exceso")
    op.drop_index(op.f("ix_autorizaciones_exceso_sim_id"), table_name="autorizaciones_exceso")
    op.drop_table("autorizaciones_exceso")

    op.drop_index(op.f("ix_limites_consumo_sim_id"), table_name="limites_consumo")
    op.drop_table("limites_consumo")

    op.drop_index(op.f("ix_consumo_numero_detectado"), table_name="consumo")
    op.drop_index(op.f("ix_consumo_sim_id"), table_name="consumo")
    op.drop_index(op.f("ix_consumo_factura_id"), table_name="consumo")
    op.drop_table("consumo")

    op.drop_index(op.f("ix_facturas_etecsa_periodo"), table_name="facturas_etecsa")
    op.drop_index(op.f("ix_facturas_etecsa_no_factura"), table_name="facturas_etecsa")
    op.drop_table("facturas_etecsa")
