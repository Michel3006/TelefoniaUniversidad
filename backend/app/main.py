import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.exc import DataError, IntegrityError

from app.api.v1.router import api_router
from app.core.config import settings

security_logger = logging.getLogger("security")


async def handler_default(request: Request, exc: Exception) -> JSONResponse:
    detail = str(exc) if settings.environment != "production" else "Error interno del servidor"
    security_logger.exception("Error no manejado", exc_info=exc)
    return JSONResponse(status_code=500, content={"detail": detail})


async def handler_integrity(request: Request, exc: IntegrityError) -> JSONResponse:
    security_logger.warning("Conflicto de integridad: %s", exc.__class__.__name__)
    return JSONResponse(
        status_code=409,
        content={"detail": "La operacion entra en conflicto con datos existentes"},
    )


async def handler_data(request: Request, exc: DataError) -> JSONResponse:
    security_logger.warning("Error de datos: %s", exc.__class__.__name__)
    return JSONResponse(
        status_code=422,
        content={"detail": "El valor enviado no es valido para el campo"},
    )


async def handler_validacion(request: Request, exc: RequestValidationError) -> JSONResponse:
    errores = " | ".join(
        f"{'.'.join(str(p) for p in e['loc'])}: {e['msg']}" for e in exc.errors()
    )
    return JSONResponse(status_code=422, content={"detail": errores})


app = FastAPI(title=settings.app_name, version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

app.add_exception_handler(IntegrityError, handler_integrity)
app.add_exception_handler(DataError, handler_data)
app.add_exception_handler(RequestValidationError, handler_validacion)
app.add_exception_handler(Exception, handler_default)

app.include_router(api_router, prefix=settings.api_prefix)


@app.get("/health")
def health():
    return {"status": "ok"}