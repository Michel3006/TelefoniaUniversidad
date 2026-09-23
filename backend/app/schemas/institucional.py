from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class CargoRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    codigo: str
    nombre: str


class AreaRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    codigo: str
    nombre: str


class SincronizacionCargo(BaseModel):
    codigo: str
    nombre: str


class SincronizacionArea(BaseModel):
    codigo: str
    nombre: str


class SincronizacionUnidad(BaseModel):
    nivel: int | None = None
    id_direccion: str
    desc_direccion: str | None = None
    id_area: str | None = None
    id_direccion_padre: str | None = None
    fecha_alta: date | None = None
    fecha_baja: date | None = None
    baja: bool = False


class SincronizacionEmpleado(BaseModel):
    id_empleado: str
    id_expediente: str | None = None
    no_ci: str | None = None
    nombre: str
    apellido_1: str
    apellido_2: str | None = None
    exttelef: str | None = None
    telefono_particular: str | None = None
    id_ccosto: str | None = None
    id_cargo: str | None = None
    id_direccion: str | None = None
    cubiculo: str | None = None
    direccion: str | None = None
    ciudad: str | None = None
    nivel: int | None = None
    baja: bool = False


class SincronizacionRrhh(BaseModel):
    cargos: list[SincronizacionCargo] = Field(default_factory=list, max_length=50_000)
    areas: list[SincronizacionArea] = Field(default_factory=list, max_length=50_000)
    unidades: list[SincronizacionUnidad] = Field(default_factory=list, max_length=50_000)
    empleados: list[SincronizacionEmpleado] = Field(default_factory=list, max_length=50_000)


class SincronizacionResumen(BaseModel):
    cargos: int
    areas: int
    unidades: int
    empleados: int