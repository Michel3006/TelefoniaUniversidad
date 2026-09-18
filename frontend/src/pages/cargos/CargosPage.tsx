import type { ColumnDef } from "@tanstack/react-table";
import { DataTable } from "../../components/ui/DataTable";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { useCargos } from "../../lib/queries";
import type { Cargo } from "../../lib/types";

const columnas: ColumnDef<Cargo, any>[] = [
  { header: "Código", accessorKey: "codigo", cell: (c) => <span className="dato">{c.getValue()}</span> },
  { header: "Cargo", accessorKey: "nombre" },
];

export function CargosPage() {
  const cargos = useCargos();

  return (
    <div className="space-y-4">
      <h1 className="text-lg font-semibold text-tinta">Cargos</h1>

      <div className="border border-filete bg-papel-alto px-4 py-3 text-sm text-neutro">
        Catálogo de cargos sincronizado desde ASSETS_RH. Solo lectura.
      </div>

      {cargos.isLoading && <EmptyState titulo="Cargando…" />}
      {cargos.isError && <ErrorState mensaje={(cargos.error as Error)?.message ?? ""} onReintentar={() => cargos.refetch()} />}
      {!cargos.isLoading && !cargos.isError && (
        <DataTable columns={columnas} data={cargos.data ?? []} vacioTitulo="Todavía no hay cargos sincronizados." />
      )}
    </div>
  );
}