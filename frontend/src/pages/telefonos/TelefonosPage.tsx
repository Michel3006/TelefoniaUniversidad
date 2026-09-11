import { useMemo, useState } from "react";
import type { ColumnDef } from "@tanstack/react-table";
import { DataTable } from "../../components/ui/DataTable";
import { SlideOver } from "../../components/ui/SlideOver";
import { ConfirmDialog } from "../../components/ui/ConfirmDialog";
import { Button } from "../../components/ui/Button";
import { TextField, TextAreaField, SelectField } from "../../components/ui/Field";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { StatusPill } from "../../components/ui/StatusPill";
import { useToast } from "../../components/ui/Toast";
import { ApiError } from "../../lib/api";
import { useFormulario } from "../../lib/useFormulario";
import { toPayload, type ReglaCampo } from "../../lib/validation";
import { useCrudMutations, useEstados, useLocales, useTelefonoDetalle, useTelefonos } from "../../lib/queries";
import type { Telefono } from "../../lib/types";

const REGLAS: ReglaCampo[] = [
  { name: "numero", label: "Número", tipo: "telefono", required: true, max: 30 },
  { name: "local_id", label: "Local", tipo: "select" },
  { name: "estado_id", label: "Estado", tipo: "select" },
  { name: "observaciones", label: "Observaciones", tipo: "textarea", max: 500 },
];

export function TelefonosPage() {
  const telefonos = useTelefonos();
  const estados = useEstados();
  const locales = useLocales();
  const { crear, actualizar, eliminar } = useCrudMutations<Telefono>("telefonos", "/telefonos");
  const { mostrar } = useToast();
  const { valores, errores, setValor, setValoresDesde, validarTodos, validarUno } = useFormulario(REGLAS);

  const [panel, setPanel] = useState<{ modo: "crear" | "editar"; item: Telefono | null } | null>(null);
  const [verId, setVerId] = useState<number | null>(null);
  const [aBorrar, setABorrar] = useState<Telefono | null>(null);

  const detalle = useTelefonoDetalle(verId);

  const nombreEstado = (id: number | null) => estados.data?.find((e) => e.id === id)?.nombre ?? null;
  const nombreLocal = (id: number | null) => {
    const l = locales.data?.find((x) => x.id === id);
    return l ? [l.piso, l.oficina].filter(Boolean).join(" · ") || `Local ${l.id}` : "—";
  };

  const columnas: ColumnDef<Telefono, any>[] = useMemo(
    () => [
      { header: "Número", accessorKey: "numero", cell: (c) => <span className="dato">{c.getValue()}</span> },
      { header: "Local", accessorKey: "local_id", cell: (c) => nombreLocal(c.getValue()) },
      { header: "Estado", accessorKey: "estado_id", cell: (c) => <StatusPill estado={nombreEstado(c.getValue())} /> },
    ],
    [estados.data, locales.data]
  );

  function abrirCrear() {
    setValoresDesde(null);
    setPanel({ modo: "crear", item: null });
  }

  function abrirEditar(t: Telefono) {
    setValoresDesde(t);
    setPanel({ modo: "editar", item: t });
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
        mostrar("Teléfono creado.");
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
      mostrar("Teléfono eliminado.");
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo eliminar.", "error");
    } finally {
      setABorrar(null);
    }
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Teléfonos</h1>
        <Button variant="primario" onClick={abrirCrear}>Crear</Button>
      </div>

      {telefonos.isLoading && <EmptyState titulo="Cargando…" />}
      {telefonos.isError && <ErrorState mensaje={(telefonos.error as Error)?.message ?? ""} onReintentar={() => telefonos.refetch()} />}
      {!telefonos.isLoading && !telefonos.isError && (
        <DataTable columns={columnas} data={telefonos.data ?? []} onVer={(t) => setVerId(t.id)} onEditar={abrirEditar} vacioTitulo="Todavía no hay teléfonos cargados." />
      )}

      <SlideOver abierto={verId !== null} titulo={detalle.data?.numero ?? "Teléfono"} onCerrar={() => setVerId(null)}>
        {detalle.isLoading && <p className="text-sm text-neutro">Cargando…</p>}
        {detalle.data && (
          <div className="space-y-5">
            <div>
              <p className="text-sm font-medium text-tinta">Ubicación</p>
              <dl className="mt-2 space-y-1 text-sm">
                <div className="flex justify-between"><dt className="text-neutro">Edificio</dt><dd>{detalle.data.edificio ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Local</dt><dd>{detalle.data.local ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Estado</dt><dd><StatusPill estado={detalle.data.estado} /></dd></div>
              </dl>
              {detalle.data.observaciones && <p className="mt-2 text-sm text-neutro">{detalle.data.observaciones}</p>}
            </div>
            <div>
              <p className="text-sm font-medium text-tinta">Extensiones</p>
              {detalle.data.extensiones.length === 0 ? (
                <p className="mt-2 text-sm text-neutro">No tiene extensiones asociadas.</p>
              ) : (
                <ul className="mt-2 divide-y divide-filete border border-filete">
                  {detalle.data.extensiones.map((ext) => (
                    <li key={ext.id} className="flex items-center justify-between px-3 py-2 text-sm">
                      <span className="dato">{ext.numero}</span>
                      <span className="text-neutro">{ext.responsable ?? "Sin asignar"}</span>
                      <StatusPill estado={ext.estado} />
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </div>
        )}
      </SlideOver>

      <SlideOver
        abierto={panel !== null}
        titulo={panel?.modo === "crear" ? "Crear teléfono" : "Editar teléfono"}
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
          <SelectField
            label="Local"
            options={(locales.data ?? []).map((l) => ({ value: l.id, label: [l.piso, l.oficina].filter(Boolean).join(" · ") || `Local ${l.id}` }))}
            value={valores.local_id ?? ""}
            error={errores.local_id}
            onChange={(e) => setValor("local_id", e.target.value)}
          />
          <SelectField label="Estado" options={(estados.data ?? []).map((e) => ({ value: e.id, label: e.nombre }))} value={valores.estado_id ?? ""} error={errores.estado_id} onChange={(e) => setValor("estado_id", e.target.value)} />
          <TextAreaField label="Observaciones" maxLength={500} value={valores.observaciones ?? ""} error={errores.observaciones} onChange={(e) => setValor("observaciones", e.target.value)} onBlur={() => validarUno("observaciones")} />
        </div>
      </SlideOver>

      <ConfirmDialog abierto={aBorrar !== null} titulo="Eliminar teléfono" descripcion="Esta acción no se puede deshacer." onConfirmar={confirmarBorrado} onCancelar={() => setABorrar(null)} />
    </div>
  );
}