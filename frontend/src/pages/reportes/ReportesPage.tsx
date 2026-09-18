import { useMemo, useState } from "react";
import type { ColumnDef } from "@tanstack/react-table";
import { DataTable } from "../../components/ui/DataTable";
import { TextField } from "../../components/ui/Field";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { StatusPill } from "../../components/ui/StatusPill";
import {
  useDispositivos,
  useExtensiones,
  useReporteConsumoPorPeriodo,
  useReporteExcesos,
  useReporteRecursosPorPersona,
  useReporteRecursosSinAsignar,
  useSims,
  useTelefonos,
} from "../../lib/queries";
import type { ConsumoPorPeriodo, ExcesoReporte, RecursosPorPersona, RecursoSuelto } from "../../lib/types";
import { formatMoneda } from "../../lib/formatters";

function Seccion({ titulo, children }: { titulo: string; children: React.ReactNode }) {
  return (
    <section className="space-y-3">
      <h2 className="text-sm font-semibold uppercase tracking-wide text-neutro">{titulo}</h2>
      {children}
    </section>
  );
}

function RecursosCard({ titulo, items, vacio }: { titulo: string; items: RecursoSuelto[]; vacio: string }) {
  return (
    <div className="border border-filete bg-papel-alto p-4">
      <p className="mb-2 text-sm font-semibold text-tinta">
        {titulo} <span className="dato text-neutro">({items.length})</span>
      </p>
      {items.length === 0 ? (
        <p className="text-sm text-neutro">{vacio}</p>
      ) : (
        <ul className="space-y-1 text-sm text-tinta">
          {items.slice(0, 8).map((r) => (
            <li key={`${r.tipo}-${r.id}`} className="flex justify-between gap-4">
              <span>{r.descripcion}</span>
              <span className="dato text-neutro">#{r.id}</span>
            </li>
          ))}
          {items.length > 8 && <li className="dato text-neutro">… y {items.length - 8} más</li>}
        </ul>
      )}
    </div>
  );
}

export function ReportesPage() {
  const [periodoExcesos, setPeriodoExcesos] = useState("");
  const [soloAutorizados, setSoloAutorizados] = useState(false);

  const consumoPorPeriodo = useReporteConsumoPorPeriodo();
  const excesos = useReporteExcesos(periodoExcesos || undefined, soloAutorizados ? true : undefined);
  const recursosPorPersona = useReporteRecursosPorPersona();
  const recursosSinAsignar = useReporteRecursosSinAsignar();

  const sims = useSims();
  const dispositivos = useDispositivos();
  const telefonos = useTelefonos();
  const extensiones = useExtensiones();

  const etiquetaRecurso = (tipo: string, id: number): string => {
    switch (tipo) {
      case "sim": {
        const s = sims.data?.find((x) => x.id === id);
        return s ? s.numero || s.iccid || `SIM ${id}` : `SIM ${id}`;
      }
      case "dispositivo": {
        const d = dispositivos.data?.find((x) => x.id === id);
        return d ? `${d.marca} ${d.modelo}` : `dispositivo ${id}`;
      }
      case "telefono": {
        const t = telefonos.data?.find((x) => x.id === id);
        return t ? t.numero : `teléfono ${id}`;
      }
      case "extension": {
        const e = extensiones.data?.find((x) => x.id === id);
        return e ? e.numero : `extensión ${id}`;
      }
      default:
        return `${tipo} ${id}`;
    }
  };

  const columnasPeriodo: ColumnDef<ConsumoPorPeriodo, any>[] = useMemo(
    () => [
      { header: "Período", accessorKey: "periodo", cell: (c) => <span className="dato">{c.getValue()}</span> },
      { header: "Registros", accessorKey: "registros", cell: (c) => <span className="dato">{c.getValue()}</span> },
      { header: "Consumo", accessorKey: "consumo", cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span> },
      { header: "Importe", accessorKey: "importe", cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span> },
      { header: "Excesos", accessorKey: "excesos", cell: (c) => <span className="dato">{c.getValue()}</span> },
      { header: "Excesos autorizados", accessorKey: "excesos_autorizados", cell: (c) => <span className="dato">{c.getValue()}</span> },
      { header: "No asociados", accessorKey: "no_asociados", cell: (c) => <span className="dato">{c.getValue()}</span> },
    ],
    []
  );

  const columnasExcesos: ColumnDef<ExcesoReporte, any>[] = useMemo(
    () => [
      { header: "Número", accessorKey: "numero", cell: (c) => <span className="dato">{c.getValue()}</span> },
      { header: "Período", accessorKey: "periodo", cell: (c) => <span className="dato">{c.getValue()}</span> },
      { header: "Consumo", accessorKey: "consumo", cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span> },
      { header: "Importe", accessorKey: "importe", cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span> },
      { header: "Límite efectivo", accessorKey: "limite_efectivo", cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span> },
      {
        header: "Autorizado",
        accessorKey: "con_autorizacion",
        cell: (c) => (c.getValue() ? <StatusPill estado="Autorizado" /> : <StatusPill estado="Sin autorización" />),
      },
    ],
    []
  );

  const columnasPersona: ColumnDef<RecursosPorPersona, any>[] = useMemo(
    () => [
      { accessorKey: "nombre", header: "Persona" },
      {
        accessorKey: "recursos",
        header: "Recursos activos",
        cell: (c) => {
          const recursos = c.getValue() as RecursosPorPersona["recursos"];
          if (recursos.length === 0) return <span className="text-neutro">Sin recursos</span>;
          return (
            <ul className="space-y-0.5">
              {recursos.map((r, i) => (
                <li key={i} className="flex gap-2">
                  <span>{etiquetaRecurso(r.tipo_recurso, r.recurso_id)}</span>
                  <span className="dato text-neutro">{r.tipo_recurso}</span>
                </li>
              ))}
            </ul>
          );
        },
      },
    ],
    [sims.data, dispositivos.data, telefonos.data, extensiones.data]
  );

  return (
    <div className="space-y-8">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Reportes</h1>
      </div>

      <Seccion titulo="Consumo por período">
        {consumoPorPeriodo.isLoading && <EmptyState titulo="Cargando…" />}
        {consumoPorPeriodo.isError && (
          <ErrorState mensaje={(consumoPorPeriodo.error as Error)?.message ?? ""} onReintentar={() => consumoPorPeriodo.refetch()} />
        )}
        {!consumoPorPeriodo.isLoading && !consumoPorPeriodo.isError && (
          <DataTable
            columns={columnasPeriodo}
            data={consumoPorPeriodo.data ?? []}
            vacioTitulo="Todavía no hay consumo importado para mostrar."
          />
        )}
      </Seccion>

      <Seccion titulo="Excesos de consumo">
        <div className="flex flex-wrap items-end gap-4">
          <div className="w-40">
            <TextField
              label="Período"
              dato
              placeholder="AAAA-MM"
              value={periodoExcesos}
              onChange={(e) => setPeriodoExcesos(e.target.value)}
            />
          </div>
          <label className="flex items-center gap-2 pb-2 text-sm text-tinta">
            <input
              type="checkbox"
              checked={soloAutorizados}
              onChange={(e) => setSoloAutorizados(e.target.checked)}
              className="h-4 w-4"
            />
            Solo autorizados
          </label>
        </div>
        {excesos.isLoading && <EmptyState titulo="Cargando…" />}
        {excesos.isError && <ErrorState mensaje={(excesos.error as Error)?.message ?? ""} onReintentar={() => excesos.refetch()} />}
        {!excesos.isLoading && !excesos.isError && (
          <DataTable columns={columnasExcesos} data={excesos.data ?? []} vacioTitulo="No hay excesos que coincidan con el filtro." />
        )}
      </Seccion>

      <Seccion titulo="Recursos por persona">
        {recursosPorPersona.isLoading && <EmptyState titulo="Cargando…" />}
        {recursosPorPersona.isError && (
          <ErrorState mensaje={(recursosPorPersona.error as Error)?.message ?? ""} onReintentar={() => recursosPorPersona.refetch()} />
        )}
        {!recursosPorPersona.isLoading && !recursosPorPersona.isError && (
          <DataTable
            columns={columnasPersona}
            data={recursosPorPersona.data ?? []}
            vacioTitulo="No hay personas con recursos asignados."
          />
        )}
      </Seccion>

      <Seccion titulo="Recursos sin asignar">
        {recursosSinAsignar.isLoading && <EmptyState titulo="Cargando…" />}
        {recursosSinAsignar.isError && (
          <ErrorState mensaje={(recursosSinAsignar.error as Error)?.message ?? ""} onReintentar={() => recursosSinAsignar.refetch()} />
        )}
        {!recursosSinAsignar.isLoading && !recursosSinAsignar.isError && recursosSinAsignar.data && (
          <div className="grid gap-4 lg:grid-cols-2">
            <RecursosCard titulo="SIMs" items={recursosSinAsignar.data.sims} vacio="Todas las SIMs están asignadas." />
            <RecursosCard titulo="Dispositivos" items={recursosSinAsignar.data.dispositivos} vacio="Todos los dispositivos están asignados." />
            <RecursosCard titulo="Teléfonos" items={recursosSinAsignar.data.telefonos} vacio="Todos los teléfonos están asignados." />
            <RecursosCard titulo="Extensiones" items={recursosSinAsignar.data.extensiones} vacio="Todas las extensiones están asignadas." />
          </div>
        )}
      </Seccion>
    </div>
  );
}