import { useMemo, useState } from "react";
import type { ColumnDef } from "@tanstack/react-table";
import { DataTable } from "../../components/ui/DataTable";
import { SlideOver } from "../../components/ui/SlideOver";
import { ConfirmDialog } from "../../components/ui/ConfirmDialog";
import { Button } from "../../components/ui/Button";
import { TextField, SelectField } from "../../components/ui/Field";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { StatusPill } from "../../components/ui/StatusPill";
import { useToast } from "../../components/ui/Toast";
import { ApiError } from "../../lib/api";
import { useFormulario } from "../../lib/useFormulario";
import { toPayload, type ReglaCampo } from "../../lib/validation";
import { useCrudMutations, useEstados, useLineaDetalle, useLineas, useOperadores, usePlanes, useSims } from "../../lib/queries";
import type { Linea } from "../../lib/types";

const REGLAS: ReglaCampo[] = [
  { name: "numero", label: "Número", tipo: "telefono", required: true, max: 30 },
  { name: "operador_id", label: "Operador", tipo: "select" },
  { name: "plan_id", label: "Plan", tipo: "select" },
  { name: "sim_id", label: "SIM", tipo: "select" },
  { name: "estado_id", label: "Estado", tipo: "select" },
];

export function LineasPage() {
  const lineas = useLineas();
  const estados = useEstados();
  const operadores = useOperadores();
  const planes = usePlanes();
  const sims = useSims();
  const { crear, actualizar, eliminar } = useCrudMutations<Linea>("lineas", "/lineas");
  const { mostrar } = useToast();
  const { valores, errores, setValor, setValoresDesde, validarTodos, validarUno } = useFormulario(REGLAS);

  const [panel, setPanel] = useState<{ modo: "crear" | "editar"; item: Linea | null } | null>(null);
  const [verId, setVerId] = useState<number | null>(null);
  const [aBorrar, setABorrar] = useState<Linea | null>(null);

  const detalle = useLineaDetalle(verId);

  const nombreEstado = (id: number | null) => estados.data?.find((e) => e.id === id)?.nombre ?? null;
  const nombreOperador = (id: number | null) => operadores.data?.find((o) => o.id === id)?.nombre ?? "—";

  const columnas: ColumnDef<Linea, any>[] = useMemo(
    () => [
      { header: "Número", accessorKey: "numero", cell: (c) => <span className="dato">{c.getValue()}</span> },
      { header: "Operador", accessorKey: "operador_id", cell: (c) => nombreOperador(c.getValue()) },
      { header: "Estado", accessorKey: "estado_id", cell: (c) => <StatusPill estado={nombreEstado(c.getValue())} /> },
    ],
    [estados.data, operadores.data]
  );

  function abrirCrear() {
    setValoresDesde(null);
    setPanel({ modo: "crear", item: null });
  }

  function abrirEditar(l: Linea) {
    setValoresDesde(l);
    setPanel({ modo: "editar", item: l });
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
        mostrar("Línea creada.");
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
      mostrar("Línea eliminada.");
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo eliminar.", "error");
    } finally {
      setABorrar(null);
    }
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Líneas</h1>
        <Button variant="primario" onClick={abrirCrear}>Crear</Button>
      </div>

      {lineas.isLoading && <EmptyState titulo="Cargando…" />}
      {lineas.isError && <ErrorState mensaje={(lineas.error as Error)?.message ?? ""} onReintentar={() => lineas.refetch()} />}
      {!lineas.isLoading && !lineas.isError && (
        <DataTable columns={columnas} data={lineas.data ?? []} onVer={(l) => setVerId(l.id)} onEditar={abrirEditar} vacioTitulo="Todavía no hay líneas cargadas." />
      )}

      <SlideOver abierto={verId !== null} titulo={detalle.data?.numero ?? "Línea"} onCerrar={() => setVerId(null)}>
        {detalle.isLoading && <p className="text-sm text-neutro">Cargando…</p>}
        {detalle.data && (
          <div className="space-y-5">
            <div>
              <p className="text-sm font-medium text-tinta">Datos generales</p>
              <dl className="mt-2 space-y-1 text-sm">
                <div className="flex justify-between"><dt className="text-neutro">Operador</dt><dd>{detalle.data.operador ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Plan</dt><dd>{detalle.data.plan ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Estado</dt><dd><StatusPill estado={detalle.data.estado} /></dd></div>
              </dl>
            </div>
            <div>
              <p className="text-sm font-medium text-tinta">SIM</p>
              <dl className="mt-2 space-y-1 text-sm">
                <div className="flex justify-between"><dt className="text-neutro">ICCID</dt><dd className="dato">{detalle.data.sim_iccid ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">IMSI</dt><dd className="dato">{detalle.data.sim_imsi ?? "—"}</dd></div>
              </dl>
            </div>
            <div>
              <p className="text-sm font-medium text-tinta">Asignación</p>
              <dl className="mt-2 space-y-1 text-sm">
                <div className="flex justify-between"><dt className="text-neutro">Dispositivo</dt><dd>{detalle.data.dispositivo ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Responsable</dt><dd>{detalle.data.responsable ?? "Sin asignar"}</dd></div>
              </dl>
            </div>
          </div>
        )}
      </SlideOver>

      <SlideOver
        abierto={panel !== null}
        titulo={panel?.modo === "crear" ? "Crear línea" : "Editar línea"}
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
          <TextField label="Número" required dato inputMode="tel" maxLength={30} value={valores.numero ?? ""} error={errores.numero} onChange={(e) => setValor("numero", e.target.value)} onBlur={() => validarUno("numero")} />
          <SelectField label="Operador" options={(operadores.data ?? []).map((o) => ({ value: o.id, label: o.nombre }))} value={valores.operador_id ?? ""} error={errores.operador_id} onChange={(e) => setValor("operador_id", e.target.value)} />
          <SelectField label="Plan" options={(planes.data ?? []).map((p) => ({ value: p.id, label: p.nombre }))} value={valores.plan_id ?? ""} error={errores.plan_id} onChange={(e) => setValor("plan_id", e.target.value)} />
          <SelectField label="SIM" options={(sims.data ?? []).map((s) => ({ value: s.id, label: s.iccid }))} value={valores.sim_id ?? ""} error={errores.sim_id} onChange={(e) => setValor("sim_id", e.target.value)} />
          <SelectField label="Estado" options={(estados.data ?? []).map((e) => ({ value: e.id, label: e.nombre }))} value={valores.estado_id ?? ""} error={errores.estado_id} onChange={(e) => setValor("estado_id", e.target.value)} />
        </div>
      </SlideOver>

      <ConfirmDialog abierto={aBorrar !== null} titulo="Eliminar línea" descripcion="Esta acción no se puede deshacer." onConfirmar={confirmarBorrado} onCancelar={() => setABorrar(null)} />
    </div>
  );
}