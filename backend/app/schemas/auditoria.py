from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AuditoriaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    fecha: datetime
    usuario_id: int | None = None
    usuario_nombre: str | None = None
    cargo: str | None = None  # rol (admin/gestor/consulta) al momento de operar
    metodo: str  # GET | POST | PUT | PATCH | DELETE
    ruta: str
    estatus: int  # codigo HTTP de la respuesta
    ip: str | None = None
    detalle: str | None = None  # descripcion legible + payload enmascarado
