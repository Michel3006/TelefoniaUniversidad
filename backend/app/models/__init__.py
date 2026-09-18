from app.models.organizacion import Departamento, Edificio, Local
from app.models.catalogos import Estado
from app.models.institucional import Area, Cargo
from app.models.personas import Persona
from app.models.telefonia import Dispositivo, Extension, Sim, Telefono
from app.models.planes import Contrato, Plan
from app.models.asignaciones import Asignacion
from app.models.costes import Coste
from app.models.consumo import AutorizacionExceso, Consumo, FacturaEtecsa, LimiteConsumo
from app.models.auth import Rol, Usuario
from app.models.historial import Historial

__all__ = [
    "Departamento",
    "Edificio",
    "Local",
    "Estado",
    "Area",
    "Cargo",
    "Persona",
    "Dispositivo",
    "Extension",
    "Sim",
    "Telefono",
    "Contrato",
    "Plan",
    "Asignacion",
    "Coste",
    "FacturaEtecsa",
    "Consumo",
    "LimiteConsumo",
    "AutorizacionExceso",
    "Rol",
    "Usuario",
    "Historial",
]
