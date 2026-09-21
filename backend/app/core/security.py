import logging
import re
from datetime import datetime, timedelta, timezone

import bcrypt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer

import jwt
from jwt import PyJWTError

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db
from app.models.auth import Usuario

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.api_prefix}/auth/login")

security_logger = logging.getLogger("security")

# Roles de sistema: no se pueden renombrar ni borrar.
ROLES_SISTEMA = ("admin", "gestor", "consulta")

_CREDENTIALS_ERROR = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Credenciales invalidas",
    headers={"WWW-Authenticate": "Bearer"},
)

_INACTIVO_ERROR = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Usuario desactivado",
    headers={"WWW-Authenticate": "Bearer"},
)

_DUMMY_HASH: str | None = None


def _dummy_hash() -> str:
    """Hash ficticio para igualar tiempos cuando el usuario no existe."""
    global _DUMMY_HASH
    if _DUMMY_HASH is None:
        _DUMMY_HASH = bcrypt.hashpw(b"hash-ficticio", bcrypt.gensalt()).decode()
    return _DUMMY_HASH


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())


def validar_politica_password(password: str) -> None:
    """Valida la politica de contrasenas del sistema. Lanza ValueError."""
    if password is None:
        raise ValueError("La contrasena es obligatoria")
    if len(password) < settings.password_min_length:
        raise ValueError(
            f"La contrasena debe tener al menos {settings.password_min_length} caracteres"
        )
    if len(password) > settings.password_max_chars:
        raise ValueError(f"La contrasena no puede superar {settings.password_max_chars} caracteres")
    if len(password.encode("utf-8")) > settings.password_max_bytes:
        raise ValueError("La contrasena es demasiado larga (maximo 72 bytes)")
    if not re.search(r"[A-Za-z]", password):
        raise ValueError("La contrasena debe contener al menos una letra")
    if not re.search(r"\d", password):
        raise ValueError("La contrasena debe contener al menos un digito")


def create_access_token(subject: str) -> str:
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=settings.access_token_expire_minutes)
    payload = {"sub": subject, "exp": expire, "iat": now}
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def get_current_user(
    request: Request,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> Usuario:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        username = payload.get("sub")
    except PyJWTError:
        raise _CREDENTIALS_ERROR

    if username is None:
        raise _CREDENTIALS_ERROR

    user = db.scalar(select(Usuario).where(Usuario.username == username))
    if user is None:
        raise _CREDENTIALS_ERROR

    if not user.activo:
        raise _INACTIVO_ERROR

    if user.password_changed_at is not None:
        emitido = payload.get("iat")
        if emitido is not None:
            try:
                import datetime as _dt

                if user.password_changed_at.tzinfo is None:
                    cambio = user.password_changed_at.replace(tzinfo=timezone.utc)
                else:
                    cambio = user.password_changed_at
                emitido_dt = _dt.datetime.fromtimestamp(emitido, tz=timezone.utc)
                if emitido_dt < cambio:
                    raise _CREDENTIALS_ERROR
            except (TypeError, OSError, OverflowError):
                raise _CREDENTIALS_ERROR

    request.state.user = user
    return user


def require_role(*roles: str):
    def checker(user: Usuario = Depends(get_current_user)) -> Usuario:
        if user.rol.nombre not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No autorizado para esta accion",
            )
        return user

    return checker