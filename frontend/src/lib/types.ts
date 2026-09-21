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
  debe_cambiar_password?: boolean;
}

export interface Cargo {
  id: number;
  codigo: string;
  nombre: string;
}

export interface Area {
  id: number;
  codigo: string;
  nombre: string;
}

export interface Persona {
  id: number;
  nombre: string;
  apellido: string;
  apellido_2: string | null;
  // Datos sensibles: el rol "consulta" no los recibe del backend.
  documento?: string | null;
  email?: string | null;
  telefono?: string | null;
  exttelef?: string | null;
  departamento_id: number | null;
  id_empleado: string | null;
  id_expediente: string | null;
  id_ccosto: string | null;
  cargo_id: number | null;
  area_id: number | null;
  baja: boolean;
}

export interface Departamento {
  id: number;
  nombre: string;
  departamento_padre_id: number | null;
  id_direccion: string | null;
  nivel: number | null;
  id_area: number | null;
  fecha_alta: string | null;
  fecha_baja: string | null;
  baja: boolean;
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
  numero: string;
  iccid: string | null;
  imsi: string | null;
  operador: string;
  plan_id: number | null;
  estado_id: number | null;
}

export interface Dispositivo {
  id: number;
  marca: string;
  modelo: string;
  imei: string;
  sim_id: number | null;
  local_id: number | null;
  estado_id: number | null;
  observaciones: string | null;
}

export interface Contrato {
  id: number;
  numero: string;
  observaciones: string | null;
  fecha_inicio: string | null;
  fecha_vencimiento: string | null;
}

export interface Plan {
  id: number;
  nombre: string;
  operador: string;
  contrato_id: number | null;
  coste_mensual: string | null;
  descripcion: string | null;
}

export interface Coste {
  id: number;
  periodo: string;
  importe: string;
  observaciones: string | null;
  departamento_id: number | null;
  sim_id: number | null;
}

export interface Asignacion {
  id: number;
  persona_id: number;
  tipo_recurso: "sim" | "dispositivo" | "extension" | "telefono" | string;
  recurso_id: number;
  fecha_inicio: string;
  fecha_fin: string | null;
  observaciones: string | null;
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

export interface SimDetalle {
  id: number;
  numero: string;
  operador: string | null;
  plan: string | null;
  iccid: string | null;
  imsi: string | null;
  estado: string | null;
  dispositivo: string | null;
  responsable: string | null;
  consumo_ultimo_periodo: number | null;
  en_exceso_ultimo_periodo: boolean | null;
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
  observaciones: string | null;
  fecha_inicio: string | null;
  fecha_vencimiento: string | null;
  planes: PlanResumen[];
}

export interface InventarioReporte {
  telefonos_fijos: number;
  sims: number;
  dispositivos: number;
  edificios: number;
  locales: number;
  personas: number;
}

export interface CostesTotalesReporte {
  importe_total: number | null;
  periodos: number;
}

export interface CostePorDepartamento {
  departamento_id: number | null;
  total: string | number;
  cantidad: number;
}

export interface CostePorPeriodo {
  periodo: string;
  total: string | number;
  cantidad: number;
}

export interface SincronizacionResumen {
  cargos: number;
  areas: number;
  unidades: number;
  empleados: number;
}

// --- Consumo ETECSA, límites y autorizaciones ---

export interface FacturaEtecsa {
  id: number;
  no_factura: string;
  numero_cliente: string | null;
  folio: string | null;
  periodo: string;
  fecha_factura: string | null;
  fecha_vencimiento: string | null;
  moneda: string;
  cuota_total: string | null;
  consumo_total: string | null;
  comision_total: string | null;
  impuesto_total: string | null;
  facturado_total: string | null;
  atraso: string | null;
  total_a_pagar: string | null;
  consumo_voz: string | null;
  consumo_sms: string | null;
  procesado_en: string;
}

export interface Consumo {
  id: number;
  factura_id: number;
  sim_id: number | null;
  numero_detectado: string;
  cuota: string;
  consumo: string;
  comision: string;
  impuesto: string;
  importe: string;
  en_exceso: boolean;
  con_autorizacion: boolean;
  limite_normal: string | null;
  limite_efectivo: string | null;
}

export interface ImportacionResumen {
  factura_id: number;
  no_factura: string;
  periodo: string;
  procesados: number;
  asociados: number;
  no_asociados: number;
  excesos: number;
  numeros_no_asociados: string[];
}

export interface LimiteConsumo {
  id: number;
  sim_id: number;
  valor_limite: string;
  vigente_desde: string;
  vigente_hasta: string | null;
  observaciones: string | null;
}

export interface AutorizacionExceso {
  id: number;
  sim_id: number;
  persona_id: number;
  limite_autorizado: string;
  fecha_inicio: string;
  fecha_fin: string | null;
  motivo: string | null;
  responsable: string | null;
  observaciones: string | null;
}

// --- Reportes de consumo ---

export interface ConsumoPorPeriodo {
  periodo: string;
  registros: number;
  consumo: string | number;
  importe: string | number;
  excesos: number;
  excesos_autorizados: number;
  no_asociados: number;
}

export interface ExcesoReporte {
  id: number;
  numero: string;
  sim_id: number | null;
  periodo: string;
  consumo: string;
  importe: string;
  limite_normal: string | null;
  limite_efectivo: string | null;
  en_exceso: boolean;
  con_autorizacion: boolean;
}

export interface RecursoSuelto {
  tipo: string;
  id: number;
  descripcion: string;
}

export interface RecursosSinAsignar {
  sims: RecursoSuelto[];
  dispositivos: RecursoSuelto[];
  telefonos: RecursoSuelto[];
  extensiones: RecursoSuelto[];
}

export interface RecursoPersona {
  tipo_recurso: string;
  recurso_id: number;
  fecha_inicio: string;
}

export interface RecursosPorPersona {
  persona_id: number;
  nombre: string;
  departamento_id: number | null;
  recursos: RecursoPersona[];
}
