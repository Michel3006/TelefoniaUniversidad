import { useMemo, useState } from "react";
import type { ColumnDef } from "@tanstack/react-table";
import { DataTable } from "../../components/ui/DataTable";
import { SlideOver } from "../../components/ui/SlideOver";
import { ConfirmDialog } from "../../components/ui/ConfirmDialog";
import { Button } from "../../components/ui/Button";
import { TextField, TextAreaField } from "../../components/ui/Field";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { useToast } from "../../components/ui/Toast";
import { ApiError } from "../../lib/api";
import { useFormulario } from "../../lib/useFormulario";
import { toPayload, type ReglaCampo } from "../../lib/validation";
import { useContratoDetalle, useContratos, useCrudMutations } from "../../lib/queries";
import type { Contrato } from "../../lib/types";
import { diasHasta, formatFecha } from "../../lib/formatters";

const REGLAS: ReglaCampo[] = [
  { name: "numero", label: "Número", tipo: "text", required: true, max: 50 },
  { name: "observaciones", label: "Observaciones", tipo: "textarea", max: 500 },
  { name: "fecha_inicio", label: "Fecha de inicio", tipo: "date" },
  { name: "fecha_vencimiento", label: "Fecha de vencimiento", tipo: "date" },
];

export function ContratosPage() {
  const contratos = useContratos();
  const { crear, actualizar, eliminar } = useCrudMutations<Contrato>("contratos", "/contratos");
  const { mostrar } = useToast();
  const { valores, errores, setValor, setValoresDesde, validarTodos, validarUno, marcarError } = useFormulario(REGLAS);

  const [panel, setPanel] = useState<{ modo: "crear" | "editar"; item: Contrato | null } | null>(null);
  const [verId, setVerId] = useState<number | null>(null);
  const [aBorrar, setABorrar] = useState<Contrato | null>(null);

  const detalle = useContratoDetalle(verId);

  const columnas: ColumnDef<Contrato, any>[] = useMemo(
    () => [
      { header: "Número", accessorKey: "numero", cell: (c) => <span className="dato">{c.getValue()}</span> },
      { header: "Vigencia", accessorKey: "fecha_vencimiento", cell: (c) => {
          const dias = diasHasta(c.getValue());
          return (
            <span className="dato">
              {formatFecha(c.getValue())}
              {dias !== null && dias <= 30 && <span className="ml-2 text-linea-baja">({dias}d)</span>}
            </span>
          );
        }
      },
    ],
    []
  );

  function abrirCrear() {
    setValoresDesde(null);
    setPanel({ modo: "crear", item: null });
  }

  function abrirEditar(c: Contrato) {
    setValoresDesde(c);
    setPanel({ modo: "editar", item: c });
  }

  async function guardar() {
    if (!validarTodos()) {
      mostrar("Revisá los campos marcados en rojo.", "error");
      return;
    }
    const inicio = valores.fecha_inicio?.trim();
    const vencimiento = valores.fecha_vencimiento?.trim();
    if (inicio && vencimiento && vencimiento < inicio) {
      marcarError("fecha_vencimiento", "La fecha de vencimiento no puede ser anterior a la de inicio.");
      mostrar("Revisá las fechas del contrato.", "error");
      return;
    }
    const payload = toPayload(REGLAS, valores);
    try {
      if (panel?.modo === "crear") {
        await crear.mutateAsync(payload);
        mostrar("Contrato creado.");
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
      mostrar("Contrato eliminado.");
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo eliminar.", "error");
    } finally {
      setABorrar(null);
    }
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Contratos</h1>
        <Button variant="primario" onClick={abrirCrear}>Crear</Button>
      </div>

      {contratos.isLoading && <EmptyState titulo="Cargando…" />}
      {contratos.isError && <ErrorState mensaje={(contratos.error as Error)?.message ?? ""} onReintentar={() => contratos.refetch()} />}
      {!contratos.isLoading && !contratos.isError && (
        <DataTable columns={columnas} data={contratos.data ?? []} onVer={(c) => setVerId(c.id)} onEditar={abrirEditar} vacioTitulo="Todavía no hay contratos cargados." />
      )}

      <SlideOver abierto={verId !== null} titulo={detalle.data?.numero ?? "Contrato"} onCerrar={() => setVerId(null)}>
        {detalle.isLoading && <p className="text-sm text-neutro">Cargando…</p>}
        {detalle.data && (
          <div className="space-y-5">
            <div>
              <p className="text-sm font-medium text-tinta">Datos generales</p>
              <dl className="mt-2 space-y-1 text-sm">
                <div className="flex justify-between"><dt className="text-neutro">Inicio</dt><dd className="dato">{formatFecha(detalle.data.fecha_inicio)}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Vencimiento</dt><dd className="dato">{formatFecha(detalle.data.fecha_vencimiento)}</dd></div>
              </dl>
              {detalle.data.observaciones && <p className="mt-2 text-sm text-neutro">{detalle.data.observaciones}</p>}
            </div>
          </div>
        )}
      </SlideOver>

      <SlideOver
        abierto={panel !== null}
        titulo={panel?.modo === "crear" ? "Crear contrato" : "Editar contrato"}
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
          <TextField label="Número" required dato maxLength={50} value={valores.numero ?? ""} error={errores.numero} onChange={(e) => setValor("numero", e.target.value)} onBlur={() => validarUno("numero")} />
          <TextField label="Fecha de inicio" type="date" dato value={valores.fecha_inicio ?? ""} error={errores.fecha_inicio} onChange={(e) => setValor("fecha_inicio", e.target.value)} onBlur={() => validarUno("fecha_inicio")} />
          <TextField label="Fecha de vencimiento" type="date" dato value={valores.fecha_vencimiento ?? ""} error={errores.fecha_vencimiento} onChange={(e) => { setValor("fecha_vencimiento", e.target.value); marcarError("fecha_vencimiento", null); }} onBlur={() => validarUno("fecha_vencimiento")} />
          <TextAreaField label="Observaciones" maxLength={500} value={valores.observaciones ?? ""} error={errores.observaciones} onChange={(e) => setValor("observaciones", e.target.value)} onBlur={() => validarUno("observaciones")} />
        </div>
      </SlideOver>

      <ConfirmDialog abierto={aBorrar !== null} titulo="Eliminar contrato" descripcion="Esta acción no se puede deshacer." onConfirmar={confirmarBorrado} onCancelar={() => setABorrar(null)} />
    </div>
  );
}