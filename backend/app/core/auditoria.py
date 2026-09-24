import json
import logging
from typing import Any, Awaitable, Callable

from fastapi import Request, Response
from jwt import InvalidTokenError, PyJWTError
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import SessionLocal
from app.models.auth import Usuario
from app.models.auditoria import Auditoria

audit_logger = logging.getLogger("auditoria")

# Campos que nunca deben quedar en el detalle de auditoría: se enmascaran
# tanto en el cuerpo de la petición como en la cadena de consulta.
CAMPOS_SENSIBLES = {
    "password",
    "password_hash",
    "contrasena",
    "contrasena_nueva",
    "contrasena_actual",
    "current_password",
    "new_password",
    "password_nueva",
    "token",
    "access_token",
    "authorization",
    "secret",
    "secret_key",
}

ANONYMOUS = "<<anonimo>>"
SENSIBLE_MSG = "<<enmascarado>>"

# Sesión usada por el middleware para escribir la auditoría. En pruebas se
# reemplaza por la fábrica de la BD de pruebas (ver tests/conftest.py).
_sesion_factory: Callable[[], Session] = SessionLocal


def usar_sesion_auditoria(factory: Callable[[], Session]) -> None:
    """Permite inyectar la fábrica de sesiones (tests) sobre la que escribir."""
    global _sesion_factory
    _sesion_factory = factory


def _enmascarar_valor(clave: str, valor: Any) -> Any:
    if clave.lower() in CAMPOS_SENSIBLES:
        return SENSIBLE_MSG
    if isinstance(valor, (dict, list)):
        return _enmascarar_datos(valor)
    return valor


def _enmascarar_datos(datos: Any) -> Any:
    """Recorre el payload y enmascara campos sensibles recursivamente."""
    if isinstance(datos, dict):
        return {k: _enmascarar_valor(k, v) for k, v in datos.items()}
    if isinstance(datos, list):
        return [_enmascarar_datos(v) for v in datos]
    return datos


def _payload_texto(datos: Any) -> str | None:
    if datos is None:
        return None
    try:
        return json.dumps(datos, ensure_ascii=False, default=str)
    except (TypeError, ValueError):
        return str(datos)


def _detalle(request: Request, cuerpo_m: Any) -> str:
    """Arma el detalle legible de la operación."""
    partes: list[str] = []
    try:
        query = request.url.query or None
        if query:
            partes.append(f"query={query[:2000]}")
    except Exception:
        pass
    if cuerpo_m not in (None, "{}", b"", ""):
        aprox = _payload_texto(cuerpo_m) or ""
        if len(aprox) > 4000:
            aprox = aprox[:4000] + "…"
        partes.append(f"datos={aprox}")
    return " · ".join(partes) if partes else ""


def _usuario_por_token(token: str | None, db: Session) -> tuple[int | None, str | None, str | None]:
    """Resuelve (id, nombre, cargo) del usuario autenticado desde su JWT.

    Se consulta la base con la sesión propia del middleware (viva), evitando
    acceder al objeto Usuario de una sesión ya cerrada. Sin token válido
    devuelve (None, ANONYMOUS, None) para las rutas públicas / tokens vencidos.
    """
    if not token:
        return None, ANONYMOUS, None
    try:
        import jwt

        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        username = payload.get("sub")
    except PyJWTError:
        return None, ANONYMOUS, None
    if not username:
        return None, ANONYMOUS, None
    user = db.scalar(select(Usuario).where(Usuario.username == username))
    if user is None:
        return None, ANONYMOUS, None
    cargo = user.rol.nombre if user.rol is not None else None
    return user.id, user.username, cargo


def _token(request: Request) -> str | None:
    auth = request.headers.get("Authorization") or request.headers.get("authorization") or ""
    if auth.lower().startswith("bearer "):
        return auth[7:].strip()
    return None


async def _leer_payload_enmascarado(request: Request) -> Any:
    """Lee el cuerpo enmascarado sin bloquear la descarga de archivos.

    JSON y formularios se enmascaran campo por campo; los binarios (PDF/subsida)
    se registran solo como marca y no se cargan en memoria adicionalmente.
    """
    try:
        if request.method not in ("POST", "PUT", "PATCH", "DELETE"):
            return None
        ct = (request.headers.get("content-type") or "").lower()
        if ct.startswith("multipart/") or ct.startswith("image/") or ct.startswith(
            "application/pdf"
        ):
            return {"tipo_archivo": ct.split(";")[0], "tamanyo": "multiparte/binario"}
        raw = await request.body()
    except Exception:
        return None
    if not raw:
        return None
    texto = raw.decode("utf-8", errors="replace")
    try:
        return _enmascarar_datos(json.loads(texto))
    except json.JSONDecodeError:
        pass
    if "application/x-www-form-urlencoded" in ct or "form-urlencoded" in ct:
        try:
            from urllib.parse import parse_qsl

            return _enmascarar_datos(dict(parse_qsl(texto)))
        except Exception:
            return {"cuerpo": _enmascarar_datos(texto[:2000])}
    return {"cuerpo": _enmascarar_datos(texto[:2000])}


def _excluir(request: Request) -> bool:
    """Rutas que no se auditan para evitar ruido y recursión."""
    if request.method == "OPTIONS":  # preflight CORS
        return True
    ruta = request.url.path
    if ruta in ("/", "/health", "/docs", "/redoc", "/openapi.json"):
        return True
    if ruta.startswith("/docs"):
        return True
    if ruta.startswith(settings.api_prefix + "/auditoria"):
        # Leer el propio registro de auditoría no debe re-auditarse: cada
        # consulta del panel generaría una fila nueva y crecería sin límite.
        return True
    return False


async def _cuerpo_con_reenvio(request: Request) -> Any:
    """Lee el payload para auditar y permite que el handler lo vuelva a leer.

    `request.body()` cachea el contenido en `request._body`; al reemplazar el
    receiver ASGI con ese contenido, los endpoints que lean el cuerpo después
    (dependencias de FastAPI, form-data, json) siguen funcionando igual.
    """
    payload = await _leer_payload_enmascarado(request)
    cuerpo = getattr(request, "_body", None)
    if cuerpo is not None:

        async def _receive():
            return {"type": "http.request", "body": cuerpo, "more_body": False}

        request._receive = _receive
    return payload


def _registrar(request: Request, estatus: int, cuerpo_m: Any) -> None:
    """Persiste una fila de auditoría (best effort, nunca rompe la petición)."""
    db = _sesion_factory()
    try:
        user_id, user_nombre, cargo = _usuario_por_token(_token(request), db)
        db.add(
            Auditoria(
                usuario_id=user_id,
                usuario_nombre=user_nombre,
                cargo=cargo,
                metodo=request.method if request.method else "?",
                ruta=request.url.path[:255],
                estatus=estatus,
                ip=request.client.host if request.client else None,
                detalle=_detalle(request, cuerpo_m),
            )
        )
        db.commit()
    except Exception:
        db.rollback()
        audit_logger.exception("No se pudo registrar la auditoría")
    finally:
        db.close()


async def auditoria_middleware(request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
    """Middleware HTTP: audita todas las operaciones del sistema (solo admin lo consulta)."""
    if _excluir(request):
        return await call_next(request)

    cuerpo_m = None
    if request.method in ("POST", "PUT", "PATCH", "DELETE"):
        cuerpo_m = await _cuerpo_con_reenvio(request)

    response = await call_next(request)

    try:
        _registrar(request, response.status_code, cuerpo_m)
    except Exception:
        audit_logger.exception("Falló el middleware de auditoría")
    return response


def ver_token_usuario(token: str | None) -> dict | None:
    """Devuelve el payload del JWT sin fallar; útil para diagnósticos."""
    if not token:
        return None
    try:
        import jwt

        return jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
    except InvalidTokenError:
        return None