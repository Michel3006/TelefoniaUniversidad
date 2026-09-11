from app.models.organizacion import Departamento, Edificio, Local
from app.models.catalogos import Estado, Operador
from app.models.personas import Persona
from app.models.telefonia import Dispositivo, Extension, Linea, Sim, Telefono
from app.models.planes import Contrato, Plan
from app.models.asignaciones import Asignacion
from app.models.costes import Coste
from app.models.auth import Rol, Usuario
from app.models.historial import Historial

__all__ = [
    "Departamento",
    "Edificio",
    "Local",
    "Estado",
    "Operador",
    "Persona",
    "Dispositivo",
    "Extension",
    "Linea",
    "Sim",
    "Telefono",
    "Contrato",
    "Plan",
    "Asignacion",
    "Coste",
    "Rol",
    "Usuario",
    "Historial",
]