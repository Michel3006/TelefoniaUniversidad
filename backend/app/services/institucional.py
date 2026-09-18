"""Integracion institucional con ASSETS_RH (SQL Server) y espejo local.

El sistema no consulta ASSETS_RH en tiempo real: un proceso de sincronizacion
(script CLI o endpoint admin) copia los catalogos y trabajadores a las tablas
locales de espejo (cargos, areas, departamentos.id_direccion, personas.*).
"""
from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.institucional import Area, Cargo
from app.models.organizacion import Departamento
from app.models.personas import Persona


def _texto(valor) -> str | None:
    if valor is None:
        return None
    valor = str(valor).strip()
    return valor or None


def _fecha(valor) -> date | None:
    if valor in (None, "", 0):
        return None
    if isinstance(valor, date):
        return valor
    try:
        return date.fromisoformat(str(valor)[:10])
    except (TypeError, ValueError):
        return None


def _booleano(valor) -> bool:
    if valor is None:
        return False
    if isinstance(valor, bool):
        return valor
    return str(valor).strip().lower() in ("1", "true", "si", "s", "verdadero")


def _entero(valor) -> int | None:
    if valor in (None, ""):
        return None
    try:
        return int(valor)
    except (TypeError, ValueError):
        return None


def conectar_rrhh():
    """Abre conexion a ASSETS_RH. Lanza RuntimeError si no esta habilitado."""
    if not settings.assets_rrhh_habilitado:
        raise RuntimeError(
            "La integracion con ASSETS_RH no esta habilitada (ASSETS_RRH_HABILITADO=true)"
        )
    if not settings.assets_rrhh_username or not settings.assets_rrhh_password:
        raise RuntimeError("Faltan credenciales ASSETS_RRH_USERNAME / ASSETS_RRH_PASSWORD")

    import pyodbc  # noqa: PLC0415

    cadena = (
        f"DRIVER={{{settings.assets_rrhh_driver}}};"
        f"SERVER={settings.assets_rrhh_server};"
        f"DATABASE={settings.assets_rrhh_database};"
        f"UID={settings.assets_rrhh_username};"
        f"PWD={settings.assets_rrhh_password};"
        "TrustServerCertificate=yes"
    )
    try:
        return pyodbc.connect(cadena)
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(f"No se pudo conectar a ASSETS_RH: {exc}") from exc


_SQL = {
    "cargos": (
        "SELECT Id_Cargo AS codigo, Desc_Cargo AS nombre "
        "FROM RH_Cargos ORDER BY Id_Cargo"
    ),
    "areas": (
        "SELECT Id_Area AS codigo, Desc_Area AS nombre "
        "FROM RH_Area_Trabajo_Actual ORDER BY Id_Area"
    ),
    "unidades": (
        "SELECT Id_Direccion AS id_direccion, Desc_Direccion AS desc_direccion, "
        "Id_Area AS id_area, Id_DireccionPadre AS id_direccion_padre, "
        "Fecha_Alta AS fecha_alta, Fecha_Baja AS fecha_baja, Baja AS baja "
        "FROM RH_Unidades_Organizativas ORDER BY Nivel, Id_Direccion"
    ),
    "empleados": (
        "SELECT Id_Empleado AS id_empleado, Id_Expediente AS id_expediente, "
        "No_CI AS no_ci, Nombre AS nombre, Apellido_1 AS apellido_1, "
        "Apellido_2 AS apellido_2, Exttelef AS exttelef, "
        "Telefono_Particular AS telefono_particular, Id_CCosto AS id_ccosto, "
        "Id_Cargo AS id_cargo, Id_Direccion AS id_direccion, "
        "Baja AS baja FROM Empleados_Gral ORDER BY Id_Empleado"
    ),
}


def _leer_filas(conn, sql: str) -> list[dict]:
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        columnas = [d[0] for d in cursor.description]
        return [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    finally:
        cursor.close()


def leer_recursos_rrhh(conn) -> dict:
    """Lee todos los recursos de ASSETS_RH en la forma canonica (snake_case)."""
    return {nombre: _leer_filas(conn, sql) for nombre, sql in _SQL.items()}


def _aplicar_cargos(db: Session, filas: list[dict]) -> int:
    cont = 0
    for fila in filas:
        codigo = _texto(fila.get("codigo"))
        nombre = _texto(fila.get("nombre"))
        if not codigo or not nombre:
            continue
        cargo = db.scalar(select(Cargo).where(Cargo.codigo == codigo))
        if cargo is None:
            db.add(Cargo(codigo=codigo, nombre=nombre))
        else:
            cargo.nombre = nombre
        cont += 1
    db.flush()
    return cont


def _aplicar_areas(db: Session, filas: list[dict]) -> int:
    cont = 0
    for fila in filas:
        codigo = _texto(fila.get("codigo"))
        nombre = _texto(fila.get("nombre"))
        if not codigo or not nombre:
            continue
        area = db.scalar(select(Area).where(Area.codigo == codigo))
        if area is None:
            db.add(Area(codigo=codigo, nombre=nombre))
        else:
            area.nombre = nombre
        cont += 1
    db.flush()
    return cont


def _aplicar_unidades(db: Session, filas: list[dict]) -> int:
    cont = 0
    for fila in filas:
        id_dir = _texto(fila.get("id_direccion"))
        if not id_dir:
            continue
        nombre = _texto(fila.get("desc_direccion"))
        depto = db.scalar(select(Departamento).where(Departamento.id_direccion == id_dir))
        if depto is None:
            depto = Departamento(id_direccion=id_dir)
            db.add(depto)
        depto.nombre = nombre or "SIN DESCRIPCION"
        depto.fecha_alta = _fecha(fila.get("fecha_alta"))
        depto.fecha_baja = _fecha(fila.get("fecha_baja"))
        depto.baja = _booleano(fila.get("baja"))
        cont += 1
    db.flush()

    for fila in filas:
        id_dir = _texto(fila.get("id_direccion"))
        if not id_dir:
            continue
        depto = db.scalar(select(Departamento).where(Departamento.id_direccion == id_dir))
        if depto is None:
            continue
        id_area = _texto(fila.get("id_area"))
        if id_area:
            area = db.scalar(select(Area).where(Area.codigo == id_area))
            depto.id_area = area.id if area else None
        id_padre = _texto(fila.get("id_direccion_padre"))
        if id_padre:
            depto.departamento_padre_id = db.scalar(
                select(Departamento.id).where(Departamento.id_direccion == id_padre)
            )
        else:
            depto.departamento_padre_id = None
    db.flush()
    return cont


def _aplicar_empleados(db: Session, filas: list[dict]) -> int:
    cont = 0
    for fila in filas:
        id_emp = _texto(fila.get("id_empleado"))
        if not id_emp:
            continue
        persona = db.scalar(select(Persona).where(Persona.id_empleado == id_emp))
        if persona is None:
            persona = Persona(id_empleado=id_emp)
            db.add(persona)
        persona.nombre = _texto(fila.get("nombre")) or persona.nombre
        persona.apellido = _texto(fila.get("apellido_1")) or persona.apellido
        persona.apellido_2 = _texto(fila.get("apellido_2"))
        persona.documento = _texto(fila.get("no_ci"))
        persona.telefono = _texto(fila.get("telefono_particular"))
        persona.exttelef = _texto(fila.get("exttelef"))
        persona.id_expediente = _texto(fila.get("id_expediente"))
        persona.id_ccosto = _texto(fila.get("id_ccosto"))
        persona.baja = _booleano(fila.get("baja"))

        id_dir = _texto(fila.get("id_direccion"))
        if id_dir:
            depto = db.scalar(select(Departamento).where(Departamento.id_direccion == id_dir))
            persona.departamento_id = depto.id if depto else None
            persona.area_id = depto.id_area if depto else None
        else:
            persona.departamento_id = None
            persona.area_id = None

        id_cargo = _texto(fila.get("id_cargo"))
        if id_cargo:
            cargo = db.scalar(select(Cargo).where(Cargo.codigo == id_cargo))
            persona.cargo_id = cargo.id if cargo else None
        else:
            persona.cargo_id = None
        cont += 1
    db.flush()
    return cont


def aplicar(db: Session, datos: dict) -> dict:
    """Sincroniza el espejo local a partir de una estructura canonica."""
    cargos = _aplicar_cargos(db, datos.get("cargos") or [])
    areas = _aplicar_areas(db, datos.get("areas") or [])
    unidades = _aplicar_unidades(db, datos.get("unidades") or [])
    empleados = _aplicar_empleados(db, datos.get("empleados") or [])
    db.commit()
    return {
        "cargos": cargos,
        "areas": areas,
        "unidades": unidades,
        "empleados": empleados,
    }


def sincronizar_desde_rrhh(db: Session) -> dict:
    """Conecta a ASSETS_RH, lee y aplica la sincronizacion completa."""
    with conectar_rrhh() as conn:
        datos = leer_recursos_rrhh(conn)
    return aplicar(db, datos)