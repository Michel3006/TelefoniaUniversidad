"""Rate limiting del login: por IP (ventana) y por usuario (bloqueo temporal).

Sin dependencias externas: estado en memoria, suficiente para una
aplicacion de institucion. Configurable desde Settings y desactivable en
tests con LOGIN_RATE_LIMIT_HABILITADO=false.
"""
import threading
import time

from fastapi import HTTPException, status

from app.core.config import settings


class LoginLimiter:
    def __init__(self) -> None:
        self._ip: dict[str, list[float]] = {}
        self._user: dict[str, list[float]] = {}
        self._lock = threading.Lock()

    def _purgar(self, d: dict, key: str, ventana_s: float) -> list[float]:
        ahora = time.time()
        d[key] = [t for t in d.get(key, []) if ahora - t < ventana_s]
        return d[key]

    def verificar(self, ip: str, username: str) -> None:
        """Lanza 429 si la IP o el usuario estan bloqueados."""
        if not settings.login_rate_limit_habilitado:
            return
        with self._lock:
            ventana_ip = settings.login_ventana_minutos * 60
            bloqueo_user = settings.login_bloqueo_minutos * 60

            ip_ints = self._purgar(self._ip, ip, ventana_ip)
            if len(ip_ints) >= settings.login_max_intentos:
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail="Demasiados intentos de inicio de sesion. Intente mas tarde.",
                )

            user_fallos = self._purgar(self._user, username, bloqueo_user)
            if len(user_fallos) >= settings.login_max_intentos:
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail="Cuenta temporalmente bloqueada por intentos fallidos.",
                )

    def registrar(self, ip: str, username: str, exitoso: bool) -> None:
        if not settings.login_rate_limit_habilitado:
            return
        with self._lock:
            ventana_ip = settings.login_ventana_minutos * 60
            bloqueo_user = settings.login_bloqueo_minutos * 60
            ahora = time.time()

            ip_ints = self._purgar(self._ip, ip, ventana_ip)
            ip_ints.append(ahora)

            if exitoso:
                self._user.pop(username, None)
            else:
                user_fallos = self._purgar(self._user, username, bloqueo_user)
                user_fallos.append(ahora)

    def reset(self) -> None:
        with self._lock:
            self._ip.clear()
            self._user.clear()


login_limiter = LoginLimiter()