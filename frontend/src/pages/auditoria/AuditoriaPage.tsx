import { useState } from "react";
import type { ColumnDef } from "@tanstack/react-table";
import { DataTable } from "../../components/ui/DataTable";
import { SelectField } from "../../components/ui/Field";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { useAuditoria, useAuditoriaResumen } from "../../lib/queries";
import type { AuditoriaItem } from "../../lib/types";
import { formatFechaHora } from "../../lib/formatters";

const METODOS: { value: string; label: string }[] = [
  { value: "GET", label: "GET" },
  { value: "POST", label: "POST" },
  { value: "PUT", label: "PUT" },
  { value: "PATCH", label: "PATCH" },
  { value: "DELETE", label: "DELETE" },
];

const CARGOS: { value: string; label: string }[] = [
  { value: "admin", label: "admin" },
  { value: "gestor", label: "gestor" },
  { value: "consulta", label: "consulta" },
];

const COLOR_METODO: Record<string, string> = {
  GET: "text-linea-ok",
  POST: "text-senal",
  PUT: "text-tinta",
  PATCH: "text-tinta",
  DELETE: "text-linea-baja",
};

export function AuditoriaPage() {
  const [metodo, setMetodo] = useState("");
  const [cargo, setCargo] = useState("");
  const [seleccion, setSeleccion] = useState<AuditoriaItem | null>(null);
  const auditoria = useAuditoria({ metodo: metodo || undefined, cargo: cargo || undefined });
  const resumen = useAuditoriaResumen();

  const columnas: ColumnDef<AuditoriaItem, any>[] = [
    {
      header: "Fecha",
      accessorKey: "fecha",
      cell: (c) => <span className="dato whitespace-nowrap">{formatFechaHora(c.getValue())}</span>,
    },
    {
      header: "Usuario",
      accessorFn: (r) => r.usuario_nombre ?? "—",
      cell: (c) => <span className="dato">{c.getValue<string>()}</span>,
    },
    {
      header: "Cargo",
      accessorKey: "cargo",
      cell: (c) => c.getValue() ?? "—",
    },
    {
      header: "Método",
      accessorKey: "metodo",
      cell: (c) => {
        const v = c.getValue<string>();
        return <span className={`font-semibold ${COLOR_METODO[v] ?? "text-tinta"}`}>{v}</span>;
      },
    },
    {
      header: "Ruta",
      accessorKey: "ruta",
      cell: (c) => <span className="dato">{c.getValue<string>()}</span>,
    },
    {
      header: "Estatus",
      accessorKey: "estatus",
      cell: (c) => {
        const v = c.getValue<number>();
        return (
          <span className={`dato ${v >= 400 ? "text-linea-baja" : v >= 300 ? "text-neutro" : "text-tinta"}`}>
            {v}
          </span>
        );
      },
    },
    {
      header: "IP",
      accessorKey: "ip",
      cell: (c) => <span className="dato text-neutro">{c.getValue() ?? "—"}</span>,
    },
  ];

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between gap-4">
        <h1 className="text-lg font-semibold text-tinta">Auditoría</h1>
        <div className="flex items-center gap-4">
          {resumen.data && resumen.data.total > 0 && (
            <span className="dato text-sm text-neutro">{resumen.data.total} operaciones</span>
          )}
          <div className="w-36">
            <SelectField
              label="Método"
              options={METODOS}
              value={metodo}
              onChange={(e) => setMetodo(e.target.value)}
              placeholder="Todos"
            />
          </div>
          <div className="w-36">
            <SelectField
              label="Cargo"
              options={CARGOS}
              value={cargo}
              onChange={(e) => setCargo(e.target.value)}
              placeholder="Todos"
            />
          </div>
        </div>
      </div>

      <div className="border border-filete bg-papel-alto p-4">
        <AuditoriaDetalle fila={seleccion} />
      </div>

      {auditoria.isLoading && <EmptyState titulo="Cargando…" />}
      {auditoria.isError && (
        <ErrorState mensaje={(auditoria.error as Error)?.message ?? ""} onReintentar={() => auditoria.refetch()} />
      )}
      {!auditoria.isLoading && !auditoria.isError && (
        <DataTable
          columns={columnas}
          data={auditoria.data ?? []}
          onVer={(fila) => setSeleccion(fila)}
          vacioTitulo="Todavía no hay operaciones registradas."
          vacioDescripcion="Las operaciones se registran a medida que se usa el sistema."
        />
      )}
    </div>
  );
}

function AuditoriaDetalle({ fila }: { fila: AuditoriaItem | null }) {
  if (!fila) {
    return (
      <p className="text-sm text-neutro">
        Seleccioná una fila para ver el detalle exacto de la operación.
      </p>
    );
  }
  return <pre className="whitespace-pre-wrap break-words text-xs text-tinta">{fila.detalle ?? "—"}</pre>;
}