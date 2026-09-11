"""initial migration

Revision ID: 001_initial
Revises:
Create Date: 2026-09-10

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "001_initial"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Roles
    op.create_table(
        "roles",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre", sa.String(50), unique=True, index=True),
        sa.Column("descripcion", sa.Text(), nullable=True),
    )

    # Usuarios
    op.create_table(
        "usuarios",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("username", sa.String(80), unique=True, index=True),
        sa.Column("email", sa.String(150), unique=True),
        sa.Column("password_hash", sa.String(255)),
        sa.Column("activo", sa.Boolean(), server_default=sa.text("true")),
        sa.Column("rol_id", sa.Integer(), sa.ForeignKey("roles.id")),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )

    # Departamentos (self-referential)
    op.create_table(
        "departamentos",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre", sa.String(150), index=True),
        sa.Column("departamento_padre_id", sa.Integer(), sa.ForeignKey("departamentos.id"), nullable=True),
    )

    # Edificios
    op.create_table(
        "edificios",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre", sa.String(150), index=True),
        sa.Column("direccion", sa.String(250), nullable=True),
    )

    # Locales
    op.create_table(
        "locales",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("edificio_id", sa.Integer(), sa.ForeignKey("edificios.id")),
        sa.Column("piso", sa.String(50), nullable=True),
        sa.Column("oficina", sa.String(50), nullable=True),
        sa.Column("descripcion", sa.String(250), nullable=True),
    )

    # Estados
    op.create_table(
        "estados",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre", sa.String(50), unique=True, index=True),
        sa.Column("descripcion", sa.Text(), nullable=True),
    )

    # Proveedores
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

    # Operadores
    op.create_table(
        "operadores",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre", sa.String(100), unique=True, index=True),
        sa.Column("descripcion", sa.Text(), nullable=True),
    )

    # Personas
    op.create_table(
        "personas",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre", sa.String(100)),
        sa.Column("apellido", sa.String(100)),
        sa.Column("documento", sa.String(30), nullable=True),
        sa.Column("email", sa.String(150), nullable=True),
        sa.Column("telefono", sa.String(50), nullable=True),
        sa.Column("departamento_id", sa.Integer(), sa.ForeignKey("departamentos.id"), nullable=True),
    )

    # Telefonos
    op.create_table(
        "telefonos",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("numero", sa.String(30), unique=True, index=True),
        sa.Column("local_id", sa.Integer(), sa.ForeignKey("locales.id"), nullable=True),
        sa.Column("estado_id", sa.Integer(), sa.ForeignKey("estados.id"), nullable=True),
        sa.Column("observaciones", sa.Text(), nullable=True),
    )

    # Extensiones
    op.create_table(
        "extensiones",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("numero", sa.String(30), index=True),
        sa.Column("telefono_id", sa.Integer(), sa.ForeignKey("telefonos.id"), nullable=True),
        sa.Column("estado_id", sa.Integer(), sa.ForeignKey("estados.id"), nullable=True),
        sa.Column("observaciones", sa.Text(), nullable=True),
    )

    # SIMs
    op.create_table(
        "sims",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("iccid", sa.String(30), unique=True),
        sa.Column("imsi", sa.String(30), nullable=True),
        sa.Column("operador_id", sa.Integer(), sa.ForeignKey("operadores.id"), nullable=True),
        sa.Column("estado_id", sa.Integer(), sa.ForeignKey("estados.id"), nullable=True),
    )

    # Contratos
    op.create_table(
        "contratos",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("numero", sa.String(50), index=True),
        sa.Column("proveedor_id", sa.Integer(), sa.ForeignKey("proveedores.id"), nullable=True),
        sa.Column("descripcion", sa.Text(), nullable=True),
        sa.Column("fecha_inicio", sa.Date(), nullable=True),
        sa.Column("fecha_vencimiento", sa.Date(), nullable=True),
    )

    # Planes
    op.create_table(
        "planes",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("nombre", sa.String(150), index=True),
        sa.Column("operador_id", sa.Integer(), sa.ForeignKey("operadores.id"), nullable=True),
        sa.Column("contrato_id", sa.Integer(), sa.ForeignKey("contratos.id"), nullable=True),
        sa.Column("coste_mensual", sa.Numeric(12, 2), nullable=True),
        sa.Column("descripcion", sa.Text(), nullable=True),
    )

    # Lineas
    op.create_table(
        "lineas",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("numero", sa.String(30), unique=True, index=True),
        sa.Column("operador_id", sa.Integer(), sa.ForeignKey("operadores.id"), nullable=True),
        sa.Column("plan_id", sa.Integer(), sa.ForeignKey("planes.id"), nullable=True),
        sa.Column("sim_id", sa.Integer(), sa.ForeignKey("sims.id"), nullable=True),
        sa.Column("estado_id", sa.Integer(), sa.ForeignKey("estados.id"), nullable=True),
    )

    # Dispositivos
    op.create_table(
        "dispositivos",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("marca", sa.String(100)),
        sa.Column("modelo", sa.String(100)),
        sa.Column("imei", sa.String(30), unique=True),
        sa.Column("linea_id", sa.Integer(), sa.ForeignKey("lineas.id"), nullable=True),
        sa.Column("local_id", sa.Integer(), sa.ForeignKey("locales.id"), nullable=True),
        sa.Column("estado_id", sa.Integer(), sa.ForeignKey("estados.id"), nullable=True),
    )

    # Asignaciones
    op.create_table(
        "asignaciones",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("persona_id", sa.Integer(), sa.ForeignKey("personas.id"), index=True),
        sa.Column("tipo_recurso", sa.String(30), index=True),
        sa.Column("recurso_id", sa.Integer(), index=True),
        sa.Column("fecha_inicio", sa.Date()),
        sa.Column("fecha_fin", sa.Date(), nullable=True),
    )

    # Costes
    op.create_table(
        "costes",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("periodo", sa.String(7), index=True),
        sa.Column("concepto", sa.String(150)),
        sa.Column("monto", sa.Numeric(12, 2)),
        sa.Column("moneda", sa.String(10), server_default="ARS"),
        sa.Column("departamento_id", sa.Integer(), sa.ForeignKey("departamentos.id"), nullable=True),
        sa.Column("linea_id", sa.Integer(), sa.ForeignKey("lineas.id"), nullable=True),
        sa.Column("contrato_id", sa.Integer(), sa.ForeignKey("contratos.id"), nullable=True),
    )

    # Historial
    op.create_table(
        "historial",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("entidad", sa.String(50), index=True),
        sa.Column("entidad_id", sa.Integer(), index=True),
        sa.Column("accion", sa.String(20)),
        sa.Column("campo", sa.String(100), nullable=True),
        sa.Column("valor_anterior", sa.Text(), nullable=True),
        sa.Column("valor_nuevo", sa.Text(), nullable=True),
        sa.Column("usuario_id", sa.Integer(), sa.ForeignKey("usuarios.id"), nullable=True),
        sa.Column("fecha", sa.DateTime(timezone=True), server_default=sa.func.now()),
    )

    # Insertar roles por defecto
    op.execute("INSERT INTO roles (nombre, descripcion) VALUES ('admin', 'Administrador del sistema')")
    op.execute("INSERT INTO roles (nombre, descripcion) VALUES ('gestor', 'Gestor de recursos')")
    op.execute("INSERT INTO roles (nombre, descripcion) VALUES ('consulta', 'Solo consulta')")


def downgrade() -> None:
    op.drop_table("historial")
    op.drop_table("costes")
    op.drop_table("asignaciones")
    op.drop_table("dispositivos")
    op.drop_table("lineas")
    op.drop_table("planes")
    op.drop_table("contratos")
    op.drop_table("sims")
    op.drop_table("extensiones")
    op.drop_table("telefonos")
    op.drop_table("personas")
    op.drop_table("operadores")
    op.drop_table("proveedores")
    op.drop_table("estados")
    op.drop_table("locales")
    op.drop_table("edificios")
    op.drop_table("departamentos")
    op.drop_table("usuarios")
    op.drop_table("roles")
