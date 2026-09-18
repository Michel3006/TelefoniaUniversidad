import { useMemo, useState } from "react";
import type { ColumnDef } from "@tanstack/react-table";
import { DataTable } from "../../components/ui/DataTable";
import { SlideOver } from "../../components/ui/SlideOver";
import { ConfirmDialog } from "../../components/ui/ConfirmDialog";
import { Button } from "../../components/ui/Button";
import { TextField, TextAreaField, SelectField } from "../../components/ui/Field";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { useToast } from "../../components/ui/Toast";
import { ApiError } from "../../lib/api";
import { useFormulario } from "../../lib/useFormulario";
import { toPayload, type ReglaCampo } from "../../lib/validation";
import {
  useCostes,
  useCrudMutations,
  useDepartamentos,
  useReporteCostesTotales,
  useSims,
} from "../../lib/queries";
import type { Coste } from "../../lib/types";
import { formatMoneda, periodoActual } from "../../lib/formatters";

const REGLAS: ReglaCampo[] = [
  { name: "periodo", label: "Período", tipo: "periodo", required: true },
  { name: "importe", label: "Importe (CUP)", tipo: "decimal", required: true },
  { name: "observaciones", label: "Observaciones", tipo: "text", max: 500 },
  { name: "departamento_id", label: "Departamento", tipo: "select" },
  { name: "sim_id", label: "SIM", tipo: "select" },
];

export function CostesPage() {
  const costes = useCostes();
  const departamentos = useDepartamentos();
  const sims = useSims();
  const totales = useReporteCostesTotales();
  const { crear, actualizar, eliminar } = useCrudMutations<Coste>("costes", "/costes");
  const { mostrar } = useToast();
  const { valores, errores, setValor, setValores, setValoresDesde, validarTodos, validarUno } = useFormulario(REGLAS);

  const [filtroPeriodo, setFiltroPeriodo] = useState("");
  const [filtroDepto, setFiltroDepto] = useState("");

  const [panel, setPanel] = useState<{ modo: "crear" | "editar"; item: Coste | null } | null>(null);
  const [aBorrar, setABorrar] = useState<Coste | null>(null);

  const nombreDepto = (id: number | null) => departamentos.data?.find((d) => d.id === id)?.nombre ?? "—";

  const items = useMemo(() => {
    let lista = costes.data ?? [];
    if (filtroPeriodo) lista = lista.filter((c) => c.periodo === filtroPeriodo);
    if (filtroDepto) lista = lista.filter((c) => c.departamento_id === Number(filtroDepto));
    return lista;
  }, [costes.data, filtroPeriodo, filtroDepto]);

  const columnas: ColumnDef<Coste, any>[] = useMemo(
    () => [
      { header: "Período", accessorKey: "periodo", cell: (c) => <span className="dato">{c.getValue()}</span> },
      { header: "Observaciones", accessorKey: "observaciones", cell: (c) => c.getValue() ?? "—" },
      { header: "Departamento", accessorKey: "departamento_id", cell: (c) => nombreDepto(c.getValue()) },
      {
        header: "Importe",
        accessorKey: "importe",
        cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span>,
      },
    ],
    [departamentos.data]
  );

  function abrirCrear() {
    setValores({ periodo: periodoActual(), importe: "", observaciones: "", departamento_id: "", sim_id: "" });
    setPanel({ modo: "crear", item: null });
  }

  function abrirEditar(c: Coste) {
    setValoresDesde(c);
    setPanel({ modo: "editar", item: c });
  }

  async function guardar() {
    if (!validarTodos()) {
      mostrar("Revisá los campos marcados en rojo.", "error");
      return;
    }
    const payload = toPayload(REGLAS, valores);
    try {
      if (panel?.modo === "crear") {
        await crear.mutateAsync(payload);
        mostrar("Costo creado.");
      } else if (panel?.item) {
        await actualizar.mutateAsync({ id: panel.item.id, payload });
        mostrar("Cambios guardados.");
      }
      setPanel(null);
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo guardar.", "error");
    }
  }

  async function confirmarBorrado() {
    if (!aBorrar) return;
    try {
      await eliminar.mutateAsync(aBorrar.id);
      mostrar("Costo eliminado.");
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo eliminar.", "error");
    } finally {
      setABorrar(null);
    }
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Costos</h1>
        <Button variant="primario" onClick={abrirCrear}>Crear</Button>
      </div>

      <div className="flex flex-wrap items-end gap-6 border-l border-filete pl-0">
        <div className="border-l border-filete px-6 first:border-l-0 first:pl-0">
          <p className="dato text-2xl font-bold text-tinta">{formatMoneda(totales.data?.importe_total)}</p>
          <p className="mt-1 text-sm text-neutro">importe total registrado (CUP)</p>
        </div>
        <div className="border-l border-filete px-6">
          <p className="dato text-2xl font-bold text-tinta">{totales.data?.periodos ?? "—"}</p>
          <p className="mt-1 text-sm text-neutro">períodos distintos</p>
        </div>
      </div>

      <div className="flex flex-wrap gap-4">
        <div className="w-40">
          <TextField label="Período" dato placeholder="AAAA-MM" value={filtroPeriodo} onChange={(e) => setFiltroPeriodo(e.target.value)} />
        </div>
        <div className="w-56">
          <SelectField
            label="Departamento"
            options={(departamentos.data ?? []).map((d) => ({ value: d.id, label: d.nombre }))}
            value={filtroDepto}
            onChange={(e) => setFiltroDepto(e.target.value)}
            placeholder="Todos"
          />
        </div>
      </div>

      {costes.isLoading && <EmptyState titulo="Cargando…" />}
      {costes.isError && <ErrorState mensaje={(costes.error as Error)?.message ?? ""} onReintentar={() => costes.refetch()} />}
      {!costes.isLoading && !costes.isError && (
        <DataTable
          columns={columnas}
          data={items}
          onEditar={abrirEditar}
          vacioTitulo={filtroPeriodo || filtroDepto ? "Ningún resultado para estos filtros." : "Todavía no hay costos cargados."}
        />
      )}

      <SlideOver
        abierto={panel !== null}
        titulo={panel?.modo === "crear" ? "Crear costo" : "Editar costo"}
        onCerrar={() => setPanel(null)}
        footer={
          <div className="flex items-center justify-between">
            {panel?.modo === "editar" && panel.item && (
              <Button variant="destructivo" onClick={() => { setABorrar(panel.item); setPanel(null); }}>Eliminar</Button>
            )}
            <div className="ml-auto flex gap-2">
              <Button variant="texto" onClick={() => setPanel(null)}>Cancelar</Button>
              <Button variant="primario" onClick={guardar}>Guardar cambios</Button>
            </div>
          </div>
        }
      >
        <div className="space-y-4">
          <TextField label="Período" required dato maxLength={7} value={valores.periodo ?? ""} error={errores.periodo} onChange={(e) => setValor("periodo", e.target.value)} onBlur={() => validarUno("periodo")} />
          <TextField label="Importe (CUP)" required dato inputMode="decimal" maxLength={15} placeholder="0.00" value={valores.importe ?? ""} error={errores.importe} onChange={(e) => setValor("importe", e.target.value)} onBlur={() => validarUno("importe")} />
          <TextAreaField label="Observaciones" maxLength={500} value={valores.observaciones ?? ""} error={errores.observaciones} onChange={(e) => setValor("observaciones", e.target.value)} onBlur={() => validarUno("observaciones")} />
          <SelectField label="Departamento" options={(departamentos.data ?? []).map((d) => ({ value: d.id, label: d.nombre }))} value={valores.departamento_id ?? ""} error={errores.departamento_id} onChange={(e) => setValor("departamento_id", e.target.value)} />
          <SelectField label="SIM" options={(sims.data ?? []).map((s) => ({ value: s.id, label: s.numero || s.iccid || `SIM ${s.id}` }))} value={valores.sim_id ?? ""} error={errores.sim_id} onChange={(e) => setValor("sim_id", e.target.value)} />
        </div>
      </SlideOver>

      <ConfirmDialog abierto={aBorrar !== null} titulo="Eliminar costo" descripcion="Esta acción no se puede deshacer." onConfirmar={confirmarBorrado} onCancelar={() => setABorrar(null)} />
    </div>
  );
}