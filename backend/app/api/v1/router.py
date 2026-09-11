from fastapi import APIRouter, Depends

from app.api.v1.endpoints import (
    asignaciones,
    auth,
    contratos,
    costes,
    departamentos,
    dispositivos,
    estados,
    extensiones,
    historial,
    lineas,
    locales,
    operadores,
    personas,
    planes,
    reportes,
    sims,
    telefonos,
)
from app.core.security import get_current_user

api_router = APIRouter()

_auth = [Depends(get_current_user)]

api_router.include_router(auth.auth_router)
api_router.include_router(auth.usuarios_router, dependencies=_auth)
api_router.include_router(auth.roles_router, dependencies=_auth)
api_router.include_router(personas.router, dependencies=_auth)
api_router.include_router(departamentos.router, dependencies=_auth)
api_router.include_router(locales.edificios_router, dependencies=_auth)
api_router.include_router(locales.locales_router, dependencies=_auth)
api_router.include_router(estados.router, dependencies=_auth)
api_router.include_router(operadores.router, dependencies=_auth)
api_router.include_router(telefonos.router, dependencies=_auth)
api_router.include_router(extensiones.router, dependencies=_auth)
api_router.include_router(lineas.router, dependencies=_auth)
api_router.include_router(dispositivos.router, dependencies=_auth)
api_router.include_router(sims.router, dependencies=_auth)
api_router.include_router(planes.router, dependencies=_auth)
api_router.include_router(contratos.router, dependencies=_auth)
api_router.include_router(asignaciones.router, dependencies=_auth)
api_router.include_router(costes.router, dependencies=_auth)
api_router.include_router(historial.router, dependencies=_auth)
api_router.include_router(reportes.router, dependencies=_auth)