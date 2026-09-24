from fastapi import APIRouter, Depends

from app.api.v1.endpoints import (
    areas,
    asignaciones,
    auditoria,
    auth,
    autorizaciones,
    cargos,
    consumo,
    contratos,
    departamentos,
    dispositivos,
    estados,
    extensiones,
    guias,
    historial,
    personas,
    reportes,
    sims,
    sincronizacion,
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
api_router.include_router(cargos.router, dependencies=_auth)
api_router.include_router(areas.router, dependencies=_auth)
api_router.include_router(sincronizacion.router, dependencies=_auth)
api_router.include_router(estados.router, dependencies=_auth)
api_router.include_router(telefonos.router, dependencies=_auth)
api_router.include_router(extensiones.router, dependencies=_auth)
api_router.include_router(sims.router, dependencies=_auth)
api_router.include_router(dispositivos.router, dependencies=_auth)
api_router.include_router(contratos.router, dependencies=_auth)
api_router.include_router(asignaciones.router, dependencies=_auth)
api_router.include_router(consumo.router, dependencies=_auth)
api_router.include_router(consumo.facturas_router, dependencies=_auth)
api_router.include_router(autorizaciones.router, dependencies=_auth)
api_router.include_router(historial.router, dependencies=_auth)
api_router.include_router(auditoria.router, dependencies=_auth)
api_router.include_router(reportes.router, dependencies=_auth)
api_router.include_router(guias.router, dependencies=_auth)
