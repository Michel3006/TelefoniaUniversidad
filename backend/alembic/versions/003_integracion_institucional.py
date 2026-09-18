"""integracion institucional: ASSETS_RH, ETECSA y costos en CUP

Revision ID: 003_integracion_institucional
Revises: 002_quitar_proveedores
Create Date: 2026-09-17

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "003_integracion_institucional"
down_revision: Union[str, None] = "002_quitar_proveedores"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Catalogos institucionales (espejo de ASSETS_RH)
    op.create_table(
        "cargos",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("codigo", sa.String(5), nullable=False),
        sa.Column("nombre", sa.String(120), nullable=False),
    )
    op.create_index(op.f("ix_cargos_codigo"), "cargos", ["codigo"], unique=True)
    op.create_index(op.f("ix_cargos_nombre"), "cargos", ["nombre"], unique=False)

    op.create_table(
        "areas",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("codigo", sa.String(3), nullable=False),
        sa.Column("nombre", sa.String(50), nullable=False),
    )
    op.create_index(op.f("ix_areas_codigo"), "areas", ["codigo"], unique=True)
    op.create_index(op.f("ix_areas_nombre"), "areas", ["nombre"], unique=False)

    # Departamentos: columnas institucionales
    with op.batch_alter_table("departamentos") as batch_op:
        batch_op.add_column(sa.Column("id_direccion", sa.String(15), nullable=True))
        batch_op.add_column(sa.Column("nivel", sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column("id_area", sa.Integer(), sa.ForeignKey("areas.id", name="fk_departamentos_id_area"), nullable=True))
        batch_op.add_column(sa.Column("fecha_alta", sa.Date(), nullable=True))
        batch_op.add_column(sa.Column("fecha_baja", sa.Date(), nullable=True))
        batch_op.add_column(sa.Column("baja", sa.Boolean(), nullable=True, server_default=sa.text("false")))
    op.create_index(op.f("ix_departamentos_id_direccion"), "departamentos", ["id_direccion"], unique=True)
    op.create_index(op.f("ix_departamentos_nivel"), "departamentos", ["nivel"], unique=False)

    # Personas: columnas institucionales
    with op.batch_alter_table("personas") as batch_op:
        batch_op.add_column(sa.Column("id_empleado", sa.String(15), nullable=True))
        batch_op.add_column(sa.Column("id_expediente", sa.String(15), nullable=True))
        batch_op.add_column(sa.Column("apellido_2", sa.String(50), nullable=True))
        batch_op.add_column(sa.Column("exttelef", sa.String(15), nullable=True))
        batch_op.add_column(sa.Column("id_ccosto", sa.String(10), nullable=True))
        batch_op.add_column(sa.Column("cargo_id", sa.Integer(), sa.ForeignKey("cargos.id", name="fk_personas_cargo_id"), nullable=True))
        batch_op.add_column(sa.Column("area_id", sa.Integer(), sa.ForeignKey("areas.id", name="fk_personas_area_id"), nullable=True))
        batch_op.add_column(sa.Column("baja", sa.Boolean(), nullable=True, server_default=sa.text("false")))
    op.create_index(op.f("ix_personas_id_empleado"), "personas", ["id_empleado"], unique=True)
    op.create_index(op.f("ix_personas_id_expediente"), "personas", ["id_expediente"], unique=False)

    # Lineas/Sims/Planes: operador pasa a ser texto fijo (ETECSA)
    with op.batch_alter_table("lineas") as batch_op:
        batch_op.drop_column("operador_id")
        batch_op.add_column(sa.Column("operador", sa.String(100), nullable=True, server_default="ETECSA"))
    with op.batch_alter_table("sims") as batch_op:
        batch_op.drop_column("operador_id")
        batch_op.add_column(sa.Column("operador", sa.String(100), nullable=True, server_default="ETECSA"))
    with op.batch_alter_table("planes") as batch_op:
        batch_op.drop_column("operador_id")
        batch_op.add_column(sa.Column("operador", sa.String(100), nullable=True, server_default="ETECSA"))

    # Contratos: descripcion -> observaciones
    with op.batch_alter_table("contratos") as batch_op:
        batch_op.alter_column("descripcion", new_column_name="observaciones")

    # Costes: nuevo modelo (importe, observaciones, sin moneda/contrato)
    with op.batch_alter_table("costes") as batch_op:
        batch_op.alter_column("monto", new_column_name="importe")
        batch_op.alter_column("concepto", new_column_name="observaciones")
        batch_op.drop_column("moneda")
        batch_op.drop_column("contrato_id")

    # Asignaciones: observaciones
    with op.batch_alter_table("asignaciones") as batch_op:
        batch_op.add_column(sa.Column("observaciones", sa.Text(), nullable=True))

    op.drop_table("operadores")

    # Semilla de estados
    estados = sa.table(
        "estados",
        sa.column("nombre", sa.String(50)),
        sa.column("descripcion", sa.Text()),
    )
    op.bulk_insert(estados, [
        {"nombre": "activo", "descripcion": "Recurso en servicio y operativo"},
        {"nombre": "inactivo", "descripcion": "Recurso sin uso temporal"},
        {"nombre": "en reparación", "descripcion": "Recurso en mantenimiento o reparación"},
        {"nombre": "baja", "descripcion": "Recurso dado de baja"},
        {"nombre": "suspendido", "descripcion": "Línea suspendida por impago o avería"},
        {"nombre": "disponible", "descripcion": "Recurso disponible para asignación"},
        {"nombre": "asignado", "descripcion": "Recurso asignado a un trabajador"},
    ])


def downgrade() -> None:
    with op.batch_alter_table("asignaciones") as batch_op:
        batch_op.drop_column("observaciones")

    with op.batch_alter_table("costes") as batch_op:
        batch_op.add_column(sa.Column("contrato_id", sa.Integer(), sa.ForeignKey("contratos.id", name="fk_costes_contrato_id"), nullable=True))
        batch_op.add_column(sa.Column("moneda", sa.String(10), nullable=True, server_default="CUP"))
        batch_op.alter_column("observaciones", new_column_name="concepto")
        batch_op.alter_column("importe", new_column_name="monto")

    with op.batch_alter_table("contratos") as batch_op:
        batch_op.alter_column("observaciones", new_column_name="descripcion")

    op.create_table(
        "operadores",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre", sa.String(100), nullable=False),
        sa.Column("descripcion", sa.Text(), nullable=True),
    )
    op.create_index(op.f("ix_operadores_nombre"), "operadores", ["nombre"], unique=True)

    with op.batch_alter_table("planes") as batch_op:
        batch_op.drop_column("operador")
        batch_op.add_column(sa.Column("operador_id", sa.Integer(), sa.ForeignKey("operadores.id", name="fk_planes_operador_id"), nullable=True))
    with op.batch_alter_table("sims") as batch_op:
        batch_op.drop_column("operador")
        batch_op.add_column(sa.Column("operador_id", sa.Integer(), sa.ForeignKey("operadores.id", name="fk_sims_operador_id"), nullable=True))
    with op.batch_alter_table("lineas") as batch_op:
        batch_op.drop_column("operador")
        batch_op.add_column(sa.Column("operador_id", sa.Integer(), sa.ForeignKey("operadores.id", name="fk_lineas_operador_id"), nullable=True))

    op.drop_index(op.f("ix_personas_id_expediente"), table_name="personas")
    op.drop_index(op.f("ix_personas_id_empleado"), table_name="personas")
    with op.batch_alter_table("personas") as batch_op:
        batch_op.drop_column("baja")
        batch_op.drop_column("area_id")
        batch_op.drop_column("cargo_id")
        batch_op.drop_column("id_ccosto")
        batch_op.drop_column("exttelef")
        batch_op.drop_column("apellido_2")
        batch_op.drop_column("id_expediente")
        batch_op.drop_column("id_empleado")

    op.drop_index(op.f("ix_departamentos_nivel"), table_name="departamentos")
    op.drop_index(op.f("ix_departamentos_id_direccion"), table_name="departamentos")
    with op.batch_alter_table("departamentos") as batch_op:
        batch_op.drop_column("baja")
        batch_op.drop_column("fecha_baja")
        batch_op.drop_column("fecha_alta")
        batch_op.drop_column("id_area")
        batch_op.drop_column("nivel")
        batch_op.drop_column("id_direccion")

    op.drop_index(op.f("ix_areas_nombre"), table_name="areas")
    op.drop_index(op.f("ix_areas_codigo"), table_name="areas")
    op.drop_table("areas")
    op.drop_index(op.f("ix_cargos_nombre"), table_name="cargos")
    op.drop_index(op.f("ix_cargos_codigo"), table_name="cargos")
    op.drop_table("cargos")