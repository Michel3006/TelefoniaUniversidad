// Hooks de TanStack Query para cada entidad. Nombres de ruta confirmados
// contra backend/app/api/v1/router.py y cada endpoints/*.py — no asumidos.
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { api, qs } from "./api";
import type {
  Area,
  Asignacion,
  AutorizacionExceso,
  Cargo,
  Consumo,
  ConsumoPorPeriodo,
  Contrato,
  ContratoDetalle,
  CostePorDepartamento,
  CostePorPeriodo,
  Coste,
  CostesTotalesReporte,
  Departamento,
  Dispositivo,
  Edificio,
  Estado,
  ExcesoReporte,
  Extension,
  FacturaEtecsa,
  HistorialItem,
  ImportacionResumen,
  InventarioReporte,
  LimiteConsumo,
  Local,
  Persona,
  Plan,
  RecursosPorPersona,
  RecursosSinAsignar,
  Rol,
  Sim,
  SimDetalle,
  SincronizacionResumen,
  Telefono,
  TelefonoDetalle,
  Usuario,
} from "./types";

const LIST_LIMIT = 500;

function listado<T>(key: string, path: string) {
  return () =>
    useQuery({
      queryKey: [key, "list"],
      queryFn: () => api<T[]>(`${path}${qs({ limit: LIST_LIMIT })}`),
    });
}

export const useEstados = listado<Estado>("estados", "/estados/");
export const usePersonas = listado<Persona>("personas", "/personas/");
export const useDepartamentos = listado<Departamento>("departamentos", "/departamentos/");
export const useCargos = listado<Cargo>("cargos", "/cargos/");
export const useAreas = listado<Area>("areas", "/areas/");
export const useEdificios = listado<Edificio>("edificios", "/edificios/");
export const useLocales = listado<Local>("locales", "/locales/");
export const useTelefonos = listado<Telefono>("telefonos", "/telefonos/");
export const useExtensiones = listado<Extension>("extensiones", "/extensiones/");
export const useDispositivos = listado<Dispositivo>("dispositivos", "/dispositivos/");
export const useSims = listado<Sim>("sims", "/sims/");
export const usePlanes = listado<Plan>("planes", "/planes/");
export const useContratos = listado<Contrato>("contratos", "/contratos/");
export const useCostes = listado<Coste>("costes", "/costes/");
export const useRoles = listado<Rol>("roles", "/roles/");
export const useUsuarios = listado<Usuario>("usuarios", "/usuarios/");

// --- Consumo ETECSA ---

export const useFacturas = listado<FacturaEtecsa>("facturas", "/facturas-etecsa/");
export const useLimites = listado<LimiteConsumo>("limites", "/limites/");
export const useAutorizaciones = listado<AutorizacionExceso>("autorizaciones", "/autorizaciones/");

export function useConsumos(params: { sim_id?: number; periodo?: string }) {
  return useQuery({
    queryKey: ["consumo", "list", params],
    queryFn: () => api<Consumo[]>(`/consumo/${qs({ ...params, limit: LIST_LIMIT })}`),
  });
}

export function useConsumoNoAsociados(periodo?: string) {
  return useQuery({
    queryKey: ["consumo", "no-asociados", periodo ?? null],
    queryFn: () => api<Consumo[]>(`/consumo/no-asociados${qs({ periodo, limit: LIST_LIMIT })}`),
  });
}

export function useConsumoExcesos(periodo?: string, autorizado?: boolean) {
  return useQuery({
    queryKey: ["consumo", "excesos", periodo ?? null, autorizado ?? null],
    queryFn: () =>
      api<Consumo[]>(
        `/consumo/excesos${qs({ periodo, autorizado: autorizado === undefined ? undefined : String(autorizado), limit: LIST_LIMIT })}`
      ),
  });
}

export function useImportarFactura() {
  const qc = useQueryClient();
  return useMutation({
    mutationFn: ({ contenido, nombre }: { contenido: Blob; nombre: string }) => {
      const fd = new FormData();
      fd.append("archivo", new File([contenido], nombre, { type: "application/pdf" }));
      return api<ImportacionResumen>("/consumo/importar-pdf", { method: "POST", formData: fd });
    },
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ["facturas"] });
      qc.invalidateQueries({ queryKey: ["consumo"] });
      qc.invalidateQueries({ queryKey: ["reportes"] });
    },
  });
}

// --- Búsquedas rápidas ---

export function useBuscarDispositivos(q: string) {
  return useQuery({
    queryKey: ["dispositivos", "buscar", q],
    queryFn: () => api<Dispositivo[]>(`/dispositivos/buscar${qs({ q })}`),
    enabled: q.trim().length > 0,
  });
}

export function useBuscarExtensiones(q: string) {
  return useQuery({
    queryKey: ["extensiones", "buscar", q],
    queryFn: () => api<Extension[]>(`/extensiones/buscar${qs({ q })}`),
    enabled: q.trim().length > 0,
  });
}

export function useBuscarTelefonos(q: string) {
  return useQuery({
    queryKey: ["telefonos", "buscar", q],
    queryFn: () => api<Telefono[]>(`/telefonos/buscar${qs({ q })}`),
    enabled: q.trim().length > 0,
  });
}

export function useBuscarSims(q: string) {
  return useQuery({
    queryKey: ["sims", "buscar", q],
    queryFn: () => api<Sim[]>(`/sims/buscar${qs({ q })}`),
    enabled: q.trim().length > 0,
  });
}

export function useBuscarPersonas(q: string) {
  return useQuery({
    queryKey: ["personas", "buscar", q],
    queryFn: () => api<Persona[]>(`/personas/buscar${qs({ q })}`),
    enabled: q.trim().length > 0,
  });
}

export function useAsignacionesActivas() {
  return useQuery({
    queryKey: ["asignaciones", "activas"],
    queryFn: () => api<Asignacion[]>("/asignaciones/activas"),
  });
}

export function useAsignacionesPorPersona(personaId: number | null) {
  return useQuery({
    queryKey: ["asignaciones", "por-persona", personaId],
    queryFn: () => api<Asignacion[]>(`/asignaciones/por-persona/${personaId}`),
    enabled: personaId != null,
  });
}

export function useAsignacionesPorRecurso(tipo: string | null, recursoId: number | null) {
  return useQuery({
    queryKey: ["asignaciones", "por-recurso", tipo, recursoId],
    queryFn: () =>
      api<Asignacion[]>(`/asignaciones/por-recurso${qs({ tipo_recurso: tipo, recurso_id: recursoId ?? undefined })}`),
    enabled: !!tipo && recursoId != null,
  });
}

export function useSimDetalle(id: number | null) {
  return useQuery({
    queryKey: ["sims", "detalle", id],
    queryFn: () => api<SimDetalle>(`/sims/${id}/detalle`),
    enabled: id != null,
  });
}

export function useTelefonoDetalle(id: number | null) {
  return useQuery({
    queryKey: ["telefonos", "detalle", id],
    queryFn: () => api<TelefonoDetalle>(`/telefonos/${id}/detalle`),
    enabled: id != null,
  });
}

export function useContratoDetalle(id: number | null) {
  return useQuery({
    queryKey: ["contratos", "detalle", id],
    queryFn: () => api<ContratoDetalle>(`/contratos/${id}/detalle`),
    enabled: id != null,
  });
}

export function useExtensionesPorTelefono(telefonoId: number | null) {
  return useQuery({
    queryKey: ["extensiones", "por-telefono", telefonoId],
    queryFn: () => api<Extension[]>(`/extensiones/por-telefono/${telefonoId}`),
    enabled: telefonoId != null,
  });
}

export function useHistorial(entidad?: string, entidadId?: number) {
  return useQuery({
    queryKey: ["historial", entidad ?? null, entidadId ?? null],
    queryFn: () => api<HistorialItem[]>(`/historial/${qs({ entidad, entidad_id: entidadId })}`),
  });
}

// --- Reportes (panel principal y página de costos) ---

export function useReporteInventario() {
  return useQuery({ queryKey: ["reportes", "inventario"], queryFn: () => api<InventarioReporte>("/reportes/inventario") });
}

export function useReporteCostesTotales() {
  return useQuery({
    queryKey: ["reportes", "costes-totales"],
    queryFn: () => api<CostesTotalesReporte>("/reportes/costes-totales"),
  });
}

export function useReporteCostesPorDepartamento() {
  return useQuery({
    queryKey: ["reportes", "costes-por-departamento"],
    queryFn: () => api<CostePorDepartamento[]>("/reportes/costes-por-departamento"),
  });
}

export function useReporteCostesPorPeriodo() {
  return useQuery({
    queryKey: ["reportes", "costes-por-periodo"],
    queryFn: () => api<CostePorPeriodo[]>("/reportes/costes-por-periodo"),
  });
}

export function useReporteConsumoPorPeriodo() {
  return useQuery({
    queryKey: ["reportes", "consumo-por-periodo"],
    queryFn: () => api<ConsumoPorPeriodo[]>("/reportes/consumo-por-periodo"),
  });
}

export function useReporteExcesos(periodo?: string, autorizado?: boolean) {
  return useQuery({
    queryKey: ["reportes", "excesos", periodo ?? null, autorizado ?? null],
    queryFn: () =>
      api<ExcesoReporte[]>(
        `/reportes/excesos${qs({ periodo, autorizado: autorizado === undefined ? undefined : String(autorizado) })}`
      ),
  });
}

export function useReporteRecursosSinAsignar() {
  return useQuery({
    queryKey: ["reportes", "recursos-sin-asignar"],
    queryFn: () => api<RecursosSinAsignar>("/reportes/recursos-sin-asignar"),
  });
}

export function useReporteRecursosPorPersona() {
  return useQuery({
    queryKey: ["reportes", "recursos-por-persona"],
    queryFn: () => api<RecursosPorPersona[]>("/reportes/recursos-por-persona"),
  });
}

// --- Sincronizacion institucional (ASSETS_RH) ---

export function useSincronizarRrhh() {
  return useMutation({
    mutationFn: () => api<SincronizacionResumen>("/sincronizacion/rrhh", { method: "POST" }),
  });
}

export function useImportarRrhh() {
  return useMutation({
    mutationFn: (payload: Record<string, unknown>) =>
      api<SincronizacionResumen>("/sincronizacion/rh-json", { method: "POST", json: payload }),
  });
}

// --- Mutaciones genéricas (crear/editar/borrar) reusadas por CrudPage ---

export function useCrudMutations<T>(entidadKey: string, basePath: string) {
  const qc = useQueryClient();
  const invalidate = () => qc.invalidateQueries({ queryKey: [entidadKey] });

  const crear = useMutation({
    mutationFn: (payload: Record<string, unknown>) => api<T>(`${basePath}/`, { method: "POST", json: payload }),
    onSuccess: invalidate,
  });

  const actualizar = useMutation({
    mutationFn: ({ id, payload }: { id: number; payload: Record<string, unknown> }) =>
      api<T>(`${basePath}/${id}`, { method: "PUT", json: payload }),
    onSuccess: invalidate,
  });

  const eliminar = useMutation({
    mutationFn: (id: number) => api<void>(`${basePath}/${id}`, { method: "DELETE" }),
    onSuccess: invalidate,
  });

  return { crear, actualizar, eliminar };
}
