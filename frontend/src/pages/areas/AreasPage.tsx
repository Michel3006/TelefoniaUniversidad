import type { ColumnDef } from "@tanstack/react-table";
import { DataTable } from "../../components/ui/DataTable";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { useAreas } from "../../lib/queries";
import type { Area } from "../../lib/types";

const columnas: ColumnDef<Area, any>[] = [
  { header: "Código", accessorKey: "codigo", cell: (c) => <span className="dato">{c.getValue()}</span> },
  { header: "Área", accessorKey: "nombre" },
];

export function AreasPage() {
  const areas = useAreas();

  return (
    <div className="space-y-4">
      <h1 className="text-lg font-semibold text-tinta">Áreas</h1>

      <div className="border border-filete bg-papel-alto px-4 py-3 text-sm text-neutro">
        Áreas de trabajo sincronizadas desde ASSETS_RH. Solo lectura.
      </div>

      {areas.isLoading && <EmptyState titulo="Cargando…" />}
      {areas.isError && <ErrorState mensaje={(areas.error as Error)?.message ?? ""} onReintentar={() => areas.refetch()} />}
      {!areas.isLoading && !areas.isError && (
        <DataTable columns={columnas} data={areas.data ?? []} vacioTitulo="Todavía no hay áreas sincronizadas." />
      )}
    </div>
  );
}