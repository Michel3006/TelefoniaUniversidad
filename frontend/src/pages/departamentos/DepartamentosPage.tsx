import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { useAreas, useDepartamentos } from "../../lib/queries";
import type { Departamento } from "../../lib/types";

function construirArbol(deptos: Departamento[], nombreArea: (id: number | null) => string): JSX.Element[] {
  const hijosDe = (padreId: number | null) => deptos.filter((d) => d.departamento_padre_id === padreId);

  function render(padreId: number | null, nivel: number): JSX.Element[] {
    return hijosDe(padreId).flatMap((d) => [
      <div
        key={d.id}
        className="flex items-center justify-between border-b border-filete py-2 pr-3 text-sm"
        style={{ paddingLeft: `${nivel * 20 + 4}px` }}
      >
        <span className="text-tinta">{d.nombre}</span>
        <span className="dato text-neutro">
          {d.id_direccion ? `Dir. ${d.id_direccion}` : ""}
          {d.id_area ? ` · ${nombreArea(d.id_area)}` : ""}
          {d.baja ? " · Baja" : ""}
        </span>
      </div>,
      ...render(d.id, nivel + 1),
    ]);
  }

  return render(null, 0);
}

export function DepartamentosPage() {
  const departamentos = useDepartamentos();
  const areas = useAreas();

  const nombreArea = (id: number | null) => areas.data?.find((a) => a.id === id)?.nombre ?? "—";

  const items = departamentos.data ?? [];

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Departamentos</h1>
      </div>

      <div className="border border-filete bg-papel-alto px-4 py-3 text-sm text-neutro">
        La estructura se sincroniza desde el sistema institucional (ASSETS_RH) y es de solo lectura. Los códigos
        de dirección y áreas se completan al ejecutar la sincronización.
      </div>

      {departamentos.isLoading && <EmptyState titulo="Cargando…" />}
      {departamentos.isError && (
        <ErrorState mensaje={(departamentos.error as Error)?.message ?? ""} onReintentar={() => departamentos.refetch()} />
      )}
      {!departamentos.isLoading && !departamentos.isError && items.length === 0 && (
        <EmptyState titulo="Todavía no hay departamentos sincronizados." />
      )}
      {!departamentos.isLoading && !departamentos.isError && items.length > 0 && (
        <div className="border border-filete bg-papel-alto px-3">{construirArbol(items, nombreArea)}</div>
      )}
    </div>
  );
}