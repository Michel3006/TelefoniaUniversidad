import { useState } from "react";
import { useHistorial } from "../../lib/queries";
import { SelectField } from "../../components/ui/Field";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { formatFechaHora } from "../../lib/formatters";

const ENTIDADES: { value: string; label: string }[] = [
  { value: "personas", label: "personas" },
  { value: "departamentos", label: "departamentos" },
  { value: "edificios", label: "edificios" },
  { value: "locales", label: "locales" },
  { value: "estados", label: "estados" },
  { value: "telefonos", label: "teléfonos" },
  { value: "extensiones", label: "extensiones" },
  { value: "dispositivos", label: "dispositivos" },
  { value: "sims", label: "SIMs" },
  { value: "planes", label: "planes" },
  { value: "contratos", label: "contratos" },
  { value: "costes", label: "costos" },
  { value: "asignaciones", label: "asignaciones" },
  { value: "facturas_etecsa", label: "facturas importadas" },
  { value: "usuarios", label: "usuarios" },
];

const ETIQUETA_ACCION: Record<string, string> = {
  creado: "Se creó",
  actualizado: "Se actualizó",
  eliminado: "Se eliminó",
  desasignado: "Se desasignó",
  importado: "Se importó",
};

export function HistorialPage() {
  const [entidad, setEntidad] = useState("");
  const historial = useHistorial(entidad || undefined);

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Historial</h1>
        <div className="w-56">
          <SelectField
            label="Entidad"
            options={ENTIDADES}
            value={entidad}
            onChange={(e) => setEntidad(e.target.value)}
            placeholder="Todas"
          />
        </div>
      </div>

      {historial.isLoading && <EmptyState titulo="Cargando…" />}
      {historial.isError && <ErrorState mensaje={(historial.error as Error)?.message ?? ""} onReintentar={() => historial.refetch()} />}
      {!historial.isLoading && !historial.isError && (historial.data ?? []).length === 0 && (
        <EmptyState titulo="No hay movimientos registrados todavía." />
      )}
      {!historial.isLoading && !historial.isError && (historial.data ?? []).length > 0 && (
        <ul className="divide-y divide-filete border border-filete bg-papel-alto">
          {historial.data!.map((h) => (
            <li key={h.id} className="flex items-start justify-between gap-4 px-4 py-3 text-sm">
              <div>
                <p className="text-tinta">
                  {ETIQUETA_ACCION[h.accion] ?? h.accion}{" "}
                  <span className="font-medium">{h.entidad}</span>{" "}
                  <span className="dato text-neutro">#{h.entidad_id}</span>
                </p>
                {h.campo && (
                  <p className="mt-0.5 text-neutro">
                    {h.campo}: <span className="dato">{h.valor_anterior ?? "—"}</span> → <span className="dato">{h.valor_nuevo ?? "—"}</span>
                  </p>
                )}
              </div>
              <span className="dato shrink-0 text-neutro">{formatFechaHora(h.fecha)}</span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
