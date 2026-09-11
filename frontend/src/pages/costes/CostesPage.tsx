import { useMemo, useState } from "react";
import type { ColumnDef } from "@tanstack/react-table";
import { DataTable } from "../../components/ui/DataTable";
import { SlideOver } from "../../components/ui/SlideOver";
import { ConfirmDialog } from "../../components/ui/ConfirmDialog";
import { Button } from "../../components/ui/Button";
import { TextField, SelectField } from "../../components/ui/Field";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { useToast } from "../../components/ui/Toast";
import { ApiError } from "../../lib/api";
import { useFormulario } from "../../lib/useFormulario";
import { toPayload, type ReglaCampo } from "../../lib/validation";
import {
  useContratos,
  useCostes,
  useCrudMutations,
  useDepartamentos,
  useLineas,
  useReporteCostesTotales,
} from "../../lib/queries";
import type { Coste } from "../../lib/types";
import { formatMoneda, periodoActual } from "../../lib/formatters";

const REGLAS: ReglaCampo[] = [
  { name: "periodo", label: "Período", tipo: "periodo", required: true },
  { name: "concepto", label: "Concepto", tipo: "text", required: true, max: 150 },
  { name: "monto", label: "Monto", tipo: "decimal", required: true },
  { name: "moneda", label: "Moneda", tipo: "text", max: 3, required: true },
  { name: "departamento_id", label: "Departamento", tipo: "select" },
  { name: "linea_id", label: "Línea", tipo: "select" },
  { name: "contrato_id", label: "Contrato", tipo: "select" },
];

export function CostesPage() {
  const costes = useCostes();
  const departamentos = useDepartamentos();
  const lineas = useLineas();
  const contratos = useContratos();
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
      { header: "Concepto", accessorKey: "concepto" },
      { header: "Departamento", accessorKey: "departamento_id", cell: (c) => nombreDepto(c.getValue()) },
      {
        header: "Monto",
        accessorKey: "monto",
        cell: (c) => <span className="dato">{formatMoneda(c.getValue(), c.row.original.moneda)}</span>,
      },
    ],
    [departamentos.data]
  );

  function abrirCrear() {
    setValores({ periodo: periodoActual(), concepto: "", monto: "", moneda: "ARS", departamento_id: "", linea_id: "", contrato_id: "" });
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
        mostrar("Coste creado.");
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
      mostrar("Coste eliminado.");
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo eliminar.", "error");
    } finally {
      setABorrar(null);
    }
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Costes</h1>
        <Button variant="primario" onClick={abrirCrear}>Crear</Button>
      </div>

      <div className="flex flex-wrap items-end gap-6 border-l border-filete pl-0">
        <div className="border-l border-filete px-6 first:border-l-0 first:pl-0">
          <p className="dato text-2xl font-bold text-tinta">{formatMoneda(totales.data?.monto_total)}</p>
          <p className="mt-1 text-sm text-neutro">monto total registrado</p>
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
          vacioTitulo={filtroPeriodo || filtroDepto ? "Ningún resultado para estos filtros." : "Todavía no hay costes cargados."}
        />
      )}

      <SlideOver
        abierto={panel !== null}
        titulo={panel?.modo === "crear" ? "Crear coste" : "Editar coste"}
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
          <TextField label="Concepto" required maxLength={150} value={valores.concepto ?? ""} error={errores.concepto} onChange={(e) => setValor("concepto", e.target.value)} onBlur={() => validarUno("concepto")} />
          <TextField label="Monto" required dato inputMode="decimal" maxLength={15} placeholder="0.00" value={valores.monto ?? ""} error={errores.monto} onChange={(e) => setValor("monto", e.target.value)} onBlur={() => validarUno("monto")} />
          <TextField label="Moneda" dato maxLength={3} value={valores.moneda ?? ""} error={errores.moneda} onChange={(e) => setValor("moneda", e.target.value)} onBlur={() => validarUno("moneda")} />
          <SelectField label="Departamento" options={(departamentos.data ?? []).map((d) => ({ value: d.id, label: d.nombre }))} value={valores.departamento_id ?? ""} error={errores.departamento_id} onChange={(e) => setValor("departamento_id", e.target.value)} />
          <SelectField label="Línea" options={(lineas.data ?? []).map((l) => ({ value: l.id, label: l.numero }))} value={valores.linea_id ?? ""} error={errores.linea_id} onChange={(e) => setValor("linea_id", e.target.value)} />
          <SelectField label="Contrato" options={(contratos.data ?? []).map((c) => ({ value: c.id, label: c.numero }))} value={valores.contrato_id ?? ""} error={errores.contrato_id} onChange={(e) => setValor("contrato_id", e.target.value)} />
        </div>
      </SlideOver>

      <ConfirmDialog abierto={aBorrar !== null} titulo="Eliminar coste" descripcion="Esta acción no se puede deshacer." onConfirmar={confirmarBorrado} onCancelar={() => setABorrar(null)} />
    </div>
  );
}