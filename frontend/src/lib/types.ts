// Tipos alineados 1:1 con los schemas Pydantic reales del backend
// (backend/app/schemas/*.py). No inventar campos: si el backend no lo
// devuelve, no va acá.

export interface Rol {
  id: number;
  nombre: string;
  descripcion: string | null;
}

export interface Usuario {
  id: number;
  username: string;
  email: string;
  activo: boolean;
  rol: Rol;
}

export interface Persona {
  id: number;
  nombre: string;
  apellido: string;
  documento: string | null;
  email: string | null;
  telefono: string | null;
  departamento_id: number | null;
}

export interface Departamento {
  id: number;
  nombre: string;
  departamento_padre_id: number | null;
}

export interface Edificio {
  id: number;
  nombre: string;
  direccion: string | null;
}

export interface Local {
  id: number;
  edificio_id: number;
  piso: string | null;
  oficina: string | null;
  descripcion: string | null;
}

export interface Estado {
  id: number;
  nombre: string;
  descripcion: string | null;
}

export interface Operador {
  id: number;
  nombre: string;
  descripcion: string | null;
}

export interface Telefono {
  id: number;
  numero: string;
  local_id: number | null;
  estado_id: number | null;
  observaciones: string | null;
}

export interface Extension {
  id: number;
  numero: string;
  telefono_id: number | null;
  estado_id: number | null;
  observaciones: string | null;
}

export interface Sim {
  id: number;
  iccid: string;
  imsi: string | null;
  operador_id: number | null;
  estado_id: number | null;
}

export interface Linea {
  id: number;
  numero: string;
  operador_id: number | null;
  plan_id: number | null;
  sim_id: number | null;
  estado_id: number | null;
}

export interface Dispositivo {
  id: number;
  marca: string;
  modelo: string;
  imei: string;
  linea_id: number | null;
  local_id: number | null;
  estado_id: number | null;
}

export interface Contrato {
  id: number;
  numero: string;
  descripcion: string | null;
  fecha_inicio: string | null;
  fecha_vencimiento: string | null;
}

export interface Plan {
  id: number;
  nombre: string;
  operador_id: number | null;
  contrato_id: number | null;
  coste_mensual: string | null;
  descripcion: string | null;
}

export interface Coste {
  id: number;
  periodo: string;
  concepto: string;
  monto: string;
  moneda: string;
  departamento_id: number | null;
  linea_id: number | null;
  contrato_id: number | null;
}

export interface Asignacion {
  id: number;
  persona_id: number;
  tipo_recurso: "linea" | "dispositivo" | "extension" | string;
  recurso_id: number;
  fecha_inicio: string;
  fecha_fin: string | null;
}

export interface HistorialItem {
  id: number;
  entidad: string;
  entidad_id: number;
  accion: "creado" | "actualizado" | "eliminado" | string;
  campo: string | null;
  valor_anterior: string | null;
  valor_nuevo: string | null;
  usuario_id: number | null;
  fecha: string;
}

// --- Respuestas armadas por endpoints custom (no son CRUD genérico) ---

export interface ExtensionResumen {
  id: number;
  numero: string;
  estado: string | null;
  responsable: string | null;
}

export interface TelefonoDetalle {
  id: number;
  numero: string;
  local: string | null;
  edificio: string | null;
  estado: string | null;
  observaciones: string | null;
  extensiones: ExtensionResumen[];
}

export interface LineaDetalle {
  id: number;
  numero: string;
  operador: string | null;
  plan: string | null;
  sim_iccid: string | null;
  sim_imsi: string | null;
  estado: string | null;
  dispositivo: string | null;
  responsable: string | null;
}

export interface PlanResumen {
  id: number;
  nombre: string;
  operador: string | null;
  coste_mensual: string | null;
}

export interface ContratoDetalle {
  id: number;
  numero: string;
  descripcion: string | null;
  fecha_inicio: string | null;
  fecha_vencimiento: string | null;
  planes: PlanResumen[];
}

export interface InventarioReporte {
  telefonos_fijos: number;
  lineas_moviles: number;
  dispositivos: number;
  edificios: number;
  locales: number;
  personas: number;
}

export interface CostesTotalesReporte {
  monto_total: number | null;
  periodos: number;
}

export interface CostePorDepartamento {
  departamento_id: number | null;
  total: string | number;
  cantidad: number;
}

export interface CostePorOperador {
  operador_id: number | null;
  total: string | number;
  cantidad: number;
}

export interface CostePorPeriodo {
  periodo: string;
  total: string | number;
  cantidad: number;
}
