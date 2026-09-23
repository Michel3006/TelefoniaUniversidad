import { useMemo, useRef, useState } from "react";
import type { ColumnDef } from "@tanstack/react-table";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { CheckCircle2, Upload } from "lucide-react";
import { DataTable } from "../../components/ui/DataTable";
import { ConfirmDialog } from "../../components/ui/ConfirmDialog";
import { Button } from "../../components/ui/Button";
import { TextField, SelectField } from "../../components/ui/Field";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { StatusPill } from "../../components/ui/StatusPill";
import { useAuth } from "../../lib/auth-context";
import { useToast } from "../../components/ui/Toast";
import { ApiError, api } from "../../lib/api";
import {
  useConsumos,
  useConsumoExcesos,
  useConsumoNoAsociados,
  useFacturas,
  useImportarFactura,
  useSims,
} from "../../lib/queries";
import type { Consumo, FacturaEtecsa, ImportacionResumen } from "../../lib/types";
import { formatFecha, formatMoneda } from "../../lib/formatters";

type Tab = "consumos" | "excesos" | "no-asociados" | "facturas";

const TABS: { id: Tab; label: string }[] = [
  { id: "consumos", label: "Consumos" },
  { id: "excesos", label: "Excesos" },
  { id: "no-asociados", label: "No asociados" },
  { id: "facturas", label: "Facturas" },
];

function ImportarPdfTarjeta() {
  const { mostrar } = useToast();
  const importar = useImportarFactura();
  const inputRef = useRef<HTMLInputElement>(null);
  const [resumen, setResumen] = useState<ImportacionResumen | null>(null);

  async function onSeleccionar(e: React.ChangeEvent<HTMLInputElement>) {
    const archivo = e.target.files?.[0];
    e.target.value = "";
    if (!archivo) return;
    if (!archivo.type.includes("pdf") && !archivo.name.toLowerCase().endsWith(".pdf")) {
      mostrar("El archivo debe ser un PDF.", "error");
      return;
    }
    try {
      const r = await importar.mutateAsync({ contenido: archivo, nombre: archivo.name });
      setResumen(r);
      mostrar("Factura importada correctamente.");
    } catch (err) {
      setResumen(null);
      mostrar(err instanceof ApiError ? err.detail : "No se pudo importar la factura.", "error");
    }
  }

  return (
    <div className="border border-filete bg-papel-alto p-4">
      <div className="flex flex-wrap items-center gap-4">
        <input ref={inputRef} type="file" accept="application/pdf,.pdf" className="hidden" onChange={onSeleccionar} />
        <Button variant="primario" onClick={() => inputRef.current?.click()} disabled={importar.isPending}>
          <Upload className="mr-2 h-4 w-4" />
          {importar.isPending ? "Procesando PDF…" : "Importar factura ETECSA (PDF)"}
        </Button>
        <p className="text-sm text-neutro">El PDF se procesa, se guarda el histórico de consumo, se registran las SIMs nuevas y se detectan excesos automáticamente.</p>
      </div>

      {resumen && (
        <div className="mt-4 flex flex-wrap items-center gap-6 border-t border-filete pt-4">
          <CheckCircle2 className="h-5 w-5 text-tinta" />
          <div className="flex flex-wrap gap-x-6 gap-y-2 text-sm">
            <span>
              Factura <span className="dato">{resumen.no_factura}</span>
            </span>
            <span>
              Período <span className="dato">{resumen.periodo}</span>
            </span>
            <span className="dato">{resumen.procesados} servicios procesados</span>
            <span className="dato">{resumen.asociados} asociados</span>
            {resumen.sims_creadas > 0 && (
              <span className="dato">{resumen.sims_creadas} SIMs creadas</span>
            )}
            {resumen.no_asociados > 0 && (
              <span className="dato">{resumen.no_asociados} sin asociar</span>
            )}
            {resumen.numeros_sims_creadas.length > 0 && (
              <span className="text-neutro">Nuevas SIMs: {resumen.numeros_sims_creadas.join(", ")}</span>
            )}
            <span className="dato">{resumen.excesos} excesos</span>
          </div>
        </div>
      )}
    </div>
  );
}

export function ConsumoPage() {
  const { user } = useAuth();
  const puedeImportar = ["admin", "gestor"].includes(user?.rol?.nombre?.toLowerCase() ?? "");

  const [tab, setTab] = useState<Tab>("consumos");
  const [periodo, setPeriodo] = useState("");
  const [simId, setSimId] = useState("");
  const [soloAutorizados, setSoloAutorizados] = useState(false);
  const [facturaABorrar, setFacturaABorrar] = useState<FacturaEtecsa | null>(null);

  const sims = useSims();
  const consumos = useConsumos({ periodo: periodo || undefined, sim_id: simId ? Number(simId) : undefined });
  const excesos = useConsumoExcesos(periodo || undefined, soloAutorizados ? true : undefined);
  const noAsociados = useConsumoNoAsociados(periodo || undefined);
  const facturas = useFacturas();
  const qc = useQueryClient();

  const eliminarFactura = useMutation({
    mutationFn: (id: number) => api<void>(`/facturas-etecsa/${id}`, { method: "DELETE" }),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ["facturas"] });
      qc.invalidateQueries({ queryKey: ["consumo"] });
    },
  });
  const { mostrar } = useToast();

  const nombreSim = (id: number | null) => {
    const s = sims.data?.find((x) => x.id === id);
    return s ? s.numero : "—";
  };

  const columnasConsumos: ColumnDef<Consumo, any>[] = useMemo(
    () => [
      { header: "Número", accessorKey: "numero_detectado", cell: (c) => <span className="dato">{c.getValue()}</span> },
      { header: "SIM", accessorKey: "sim_id", cell: (c) => <span className="dato">{nombreSim(c.getValue() as number | null)}</span> },
      { header: "Cuota", accessorKey: "cuota", cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span> },
      { header: "Consumo", accessorKey: "consumo", cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span> },
      { header: "Comisión", accessorKey: "comision", cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span> },
      { header: "Importe", accessorKey: "importe", cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span> },
      {
        header: "Estado",
        accessorKey: "en_exceso",
        cell: (c) => {
          const fila = c.row.original;
          if (!fila.en_exceso) return <span className="text-sm text-neutro">Dentro del límite</span>;
          return fila.con_autorizacion ? <StatusPill estado="Exceso autorizado" /> : <StatusPill estado="En exceso" />;
        },
      },
    ],
    [sims.data]
  );

  const columnasExcesos: ColumnDef<Consumo, any>[] = useMemo(
    () => [
      { header: "Número", accessorKey: "numero_detectado", cell: (c) => <span className="dato">{c.getValue()}</span> },
      { header: "Consumo", accessorKey: "consumo", cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span> },
      { header: "Límite", accessorKey: "limite_efectivo", cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span> },
      { header: "Importe", accessorKey: "importe", cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span> },
      {
        header: "Tipo",
        accessorKey: "con_autorizacion",
        cell: (c) => (c.getValue() ? <StatusPill estado="Autorizado" /> : <StatusPill estado="Sin autorización" />),
      },
    ],
    []
  );

  const columnasFacturas: ColumnDef<FacturaEtecsa, any>[] = useMemo(
    () => [
      { header: "No. factura", accessorKey: "no_factura", cell: (c) => <span className="dato">{c.getValue()}</span> },
      { header: "Período", accessorKey: "periodo", cell: (c) => <span className="dato">{c.getValue()}</span> },
      { header: "Emisión", accessorKey: "fecha_factura", cell: (c) => formatFecha(c.getValue()) },
      { header: "Vencimiento", accessorKey: "fecha_vencimiento", cell: (c) => formatFecha(c.getValue()) },
      { header: "Total a pagar", accessorKey: "total_a_pagar", cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span> },
    ],
    []
  );

  async function confirmarBorradoFactura() {
    if (!facturaABorrar) return;
    try {
      await eliminarFactura.mutateAsync(facturaABorrar.id);
      mostrar("Factura eliminada. Podés volver a importarla si corregiste el PDF.");
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo eliminar la factura.", "error");
    } finally {
      setFacturaABorrar(null);
    }
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Consumo ETECSA</h1>
      </div>

      {puedeImportar && <ImportarPdfTarjeta />}

      <div className="flex flex-wrap gap-4">
        {TABS.map((t) => (
          <button
            key={t.id}
            onClick={() => setTab(t.id)}
            className={`border-b-2 pb-1 text-sm font-medium ${
              tab === t.id ? "border-tinta text-tinta" : "border-transparent text-neutro hover:text-tinta"
            }`}
          >
            {t.label}
          </button>
        ))}
      </div>

      <div className="flex flex-wrap items-end gap-4">
        <div className="w-40">
          <TextField label="Período" dato placeholder="AAAA-MM" value={periodo} onChange={(e) => setPeriodo(e.target.value)} />
        </div>
        {(tab === "consumos" || tab === "facturas") && (
          <div className="w-56">
            <SelectField
              label="SIM"
              options={(sims.data ?? []).map((s) => ({ value: s.id, label: s.numero || s.iccid || `SIM ${s.id}` }))}
              value={simId}
              onChange={(e) => setSimId(e.target.value)}
              placeholder="Todas"
            />
          </div>
        )}
        {tab === "excesos" && (
          <label className="flex items-center gap-2 pb-2 text-sm text-tinta">
            <input
              type="checkbox"
              checked={soloAutorizados}
              onChange={(e) => setSoloAutorizados(e.target.checked)}
              className="h-4 w-4"
            />
            Solo excesos autorizados
          </label>
        )}
      </div>

      {tab === "consumos" && (
        <>
          {consumos.isLoading && <EmptyState titulo="Cargando…" />}
          {consumos.isError && <ErrorState mensaje={(consumos.error as Error)?.message ?? ""} onReintentar={() => consumos.refetch()} />}
          {!consumos.isLoading && !consumos.isError && (
            <DataTable
              columns={columnasConsumos}
              data={consumos.data ?? []}
              vacioTitulo={periodo ? "Ningún consumo en este período." : "Todavía no se importó ninguna factura de consumo."}
            />
          )}
        </>
      )}

      {tab === "excesos" && (
        <>
          {excesos.isLoading && <EmptyState titulo="Cargando…" />}
          {excesos.isError && <ErrorState mensaje={(excesos.error as Error)?.message ?? ""} onReintentar={() => excesos.refetch()} />}
          {!excesos.isLoading && !excesos.isError && (
            <DataTable
              columns={columnasExcesos}
              data={excesos.data ?? []}
              vacioTitulo={soloAutorizados ? "No hay excesos autorizados en este período." : "No hay consumos en exceso."}
            />
          )}
        </>
      )}

      {tab === "no-asociados" && (
        <>
          {noAsociados.isLoading && <EmptyState titulo="Cargando…" />}
          {noAsociados.isError && <ErrorState mensaje={(noAsociados.error as Error)?.message ?? ""} onReintentar={() => noAsociados.refetch()} />}
          {!noAsociados.isLoading && !noAsociados.isError && (
            <DataTable
              columns={columnasConsumos}
              data={noAsociados.data ?? []}
              vacioTitulo="Todas las facturas importadas tienen su SIM asociada."
              vacioDescripcion="Los números fijos que no coinciden con una SIM registrada aparecen aquí; los móviles se registran automáticamente."
            />
          )}
        </>
      )}

      {tab === "facturas" && (
        <>
          {facturas.isLoading && <EmptyState titulo="Cargando…" />}
          {facturas.isError && <ErrorState mensaje={(facturas.error as Error)?.message ?? ""} onReintentar={() => facturas.refetch()} />}
          {!facturas.isLoading && !facturas.isError && (
            <DataTable
              columns={columnasFacturas}
              data={facturas.data ?? []}
              onBorrar={puedeImportar ? (f) => setFacturaABorrar(f) : undefined}
              vacioTitulo="Todavía no se importó ninguna factura."
            />
          )}
        </>
      )}

      <ConfirmDialog
        abierto={facturaABorrar !== null}
        titulo="Eliminar factura"
        descripcion={
          facturaABorrar
            ? `Se va a eliminar la factura ${facturaABorrar.no_factura} y todo su consumo asociado. Podrás volver a importar el PDF corregido.`
            : ""
        }
        onConfirmar={confirmarBorradoFactura}
        onCancelar={() => setFacturaABorrar(null)}
      />
    </div>
  );
}