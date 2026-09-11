// Hooks de TanStack Query para cada entidad. Nombres de ruta confirmados
// contra backend/app/api/v1/router.py y cada endpoints/*.py — no asumidos.
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { api, qs } from "./api";
import type {
  Asignacion,
  Contrato,
  ContratoDetalle,
  CostePorDepartamento,
  CostePorOperador,
  CostePorPeriodo,
  Coste,
  CostesTotalesReporte,
  Departamento,
  Dispositivo,
  Edificio,
  Estado,
  Extension,
  HistorialItem,
  InventarioReporte,
  Linea,
  LineaDetalle,
  Local,
  Operador,
  Persona,
  Plan,
  Rol,
  Sim,
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
export const useOperadores = listado<Operador>("operadores", "/operadores/");
export const usePersonas = listado<Persona>("personas", "/personas/");
export const useDepartamentos = listado<Departamento>("departamentos", "/departamentos/");
export const useEdificios = listado<Edificio>("edificios", "/edificios/");
export const useLocales = listado<Local>("locales", "/locales/");
export const useTelefonos = listado<Telefono>("telefonos", "/telefonos/");
export const useExtensiones = listado<Extension>("extensiones", "/extensiones/");
export const useLineas = listado<Linea>("lineas", "/lineas/");
export const useDispositivos = listado<Dispositivo>("dispositivos", "/dispositivos/");
export const useSims = listado<Sim>("sims", "/sims/");
export const usePlanes = listado<Plan>("planes", "/planes/");
export const useContratos = listado<Contrato>("contratos", "/contratos/");
export const useCostes = listado<Coste>("costes", "/costes/");
export const useRoles = listado<Rol>("roles", "/roles/");
export const useUsuarios = listado<Usuario>("usuarios", "/usuarios/");

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

export function useLineaDetalle(id: number | null) {
  return useQuery({
    queryKey: ["lineas", "detalle", id],
    queryFn: () => api<LineaDetalle>(`/lineas/${id}/detalle`),
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

export function useReporteCostesPorOperador() {
  return useQuery({
    queryKey: ["reportes", "costes-por-operador"],
    queryFn: () => api<CostePorOperador[]>("/reportes/costes-por-operador"),
  });
}

export function useReporteCostesPorPeriodo() {
  return useQuery({
    queryKey: ["reportes", "costes-por-periodo"],
    queryFn: () => api<CostePorPeriodo[]>("/reportes/costes-por-periodo"),
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
