import { useMemo, useState } from "react";
import type { ColumnDef } from "@tanstack/react-table";
import { DataTable } from "../../components/ui/DataTable";
import { SlideOver } from "../../components/ui/SlideOver";
import { Button } from "../../components/ui/Button";
import { SelectField, TextAreaField, TextField } from "../../components/ui/Field";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { useToast } from "../../components/ui/Toast";
import { ApiError, api } from "../../lib/api";
import { useFormulario } from "../../lib/useFormulario";
import { toPayload, type ReglaCampo } from "../../lib/validation";
import { useAsignacionesActivas, useCrudMutations, useDispositivos, useExtensiones, usePersonas, useSims, useTelefonos } from "../../lib/queries";
import type { Asignacion } from "../../lib/types";
import { formatFecha } from "../../lib/formatters";
import { useQueryClient } from "@tanstack/react-query";

const TIPOS = [
  { value: "sim", label: "SIM" },
  { value: "telefono", label: "Teléfono" },
  { value: "dispositivo", label: "Dispositivo" },
  { value: "extension", label: "Extensión" },
];

const REGLAS: ReglaCampo[] = [
  { name: "persona_id", label: "Persona", tipo: "select", required: true },
  { name: "tipo_recurso", label: "Tipo de recurso", tipo: "select", required: true },
  { name: "recurso_id", label: "Recurso", tipo: "select", required: true },
  { name: "fecha_inicio", label: "Fecha de inicio", tipo: "date", required: true },
  { name: "observaciones", label: "Observaciones", tipo: "text", max: 500 },
];

export function AsignacionesPage() {
  const [verHistoricas, setVerHistoricas] = useState(false);
  const activas = useAsignacionesActivas();
  const personas = usePersonas();
  const sims = useSims();
  const telefonos = useTelefonos();
  const dispositivos = useDispositivos();
  const extensiones = useExtensiones();
  const { crear } = useCrudMutations<Asignacion>("asignaciones", "/asignaciones");
  const { mostrar } = useToast();
  const qc = useQueryClient();

  const [panel, setPanel] = useState(false);
  const { valores, errores, setValor, setValores, validarTodos } = useFormulario(REGLAS);
  const abrirPanel = () => {
    setValores({ persona_id: "", tipo_recurso: "sim", recurso_id: "", fecha_inicio: new Date().toISOString().slice(0, 10), observaciones: "" });
    setPanel(true);
  };

  const nombrePersona = (id: number) => {
    const p = personas.data?.find((x) => x.id === id);
    return p ? `${p.nombre} ${p.apellido}` : `Persona ${id}`;
  };

  const nombreRecurso = (tipo: string, id: number) => {
    if (tipo === "sim") {
      const s = sims.data?.find((x) => x.id === id);
      return s ? s.numero || s.iccid || `SIM ${s.id}` : `#${id}`;
    }
    if (tipo === "telefono") return telefonos.data?.find((t) => t.id === id)?.numero ?? `#${id}`;
    if (tipo === "dispositivo") {
      const d = dispositivos.data?.find((x) => x.id === id);
      return d ? `${d.marca} ${d.modelo}` : `#${id}`;
    }
    if (tipo === "extension") return extensiones.data?.find((e) => e.id === id)?.numero ?? `#${id}`;
    return `#${id}`;
  };

  const items = useMemo(() => activas.data ?? [], [activas.data]);

  const columnas: ColumnDef<Asignacion, any>[] = [
    { header: "Persona", accessorKey: "persona_id", cell: (c) => nombrePersona(c.getValue()) },
    { header: "Tipo", accessorKey: "tipo_recurso", cell: (c) => <span className="capitalize">{c.getValue()}</span> },
    { header: "Recurso", accessorFn: (a) => a, cell: (c) => <span className="dato">{nombreRecurso(c.row.original.tipo_recurso, c.row.original.recurso_id)}</span> },
    { header: "Desde", accessorKey: "fecha_inicio", cell: (c) => <span className="dato">{formatFecha(c.getValue())}</span> },
  ];

  async function finalizar(a: Asignacion) {
    try {
      await api(`/asignaciones/${a.id}/finalizar`, { method: "PUT" });
      mostrar("Asignación finalizada.");
      qc.invalidateQueries({ queryKey: ["asignaciones"] });
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo finalizar.", "error");
    }
  }

  async function guardar() {
    if (!validarTodos()) {
      mostrar("Revisá los campos marcados en rojo.", "error");
      return;
    }
    const payload = toPayload(REGLAS, valores);
    try {
      await crear.mutateAsync(payload);
      mostrar("Asignación creada.");
      setPanel(false);
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo crear la asignación.", "error");
    }
  }

  const opcionesRecurso = valores.tipo_recurso === "sim"
    ? (sims.data ?? []).map((s) => ({ value: s.id, label: s.numero || s.iccid || `SIM ${s.id}` }))
    : valores.tipo_recurso === "telefono"
    ? (telefonos.data ?? []).map((t) => ({ value: t.id, label: t.numero }))
    : valores.tipo_recurso === "dispositivo"
    ? (dispositivos.data ?? []).map((d) => ({ value: d.id, label: `${d.marca} ${d.modelo}` }))
    : (extensiones.data ?? []).map((e) => ({ value: e.id, label: e.numero }));

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Asignaciones</h1>
        <div className="flex items-center gap-4">
          <button
            onClick={() => setVerHistoricas((v) => !v)}
            className="text-sm text-neutro underline-offset-2 hover:text-tinta hover:underline"
          >
            {verHistoricas ? "Ver solo activas" : "Ver históricas"}
          </button>
          <Button variant="primario" onClick={() => abrirPanel()}>Asignar recurso</Button>
        </div>
      </div>

      {verHistoricas ? (
        <EmptyState
          titulo="El historial completo de asignaciones (activas y finalizadas) está en la página de Historial."
          descripcion="Filtrá ahí por entidad “asignaciones” para ver altas, bajas y finalizaciones."
        />
      ) : (
        <>
          {activas.isLoading && <EmptyState titulo="Cargando…" />}
          {activas.isError && <ErrorState mensaje={(activas.error as Error)?.message ?? ""} onReintentar={() => activas.refetch()} />}
          {!activas.isLoading && !activas.isError && (
            <DataTable
              columns={columnas}
              data={items}
              onEditar={finalizar}
              vacioTitulo="No hay asignaciones activas."
            />
          )}
          <p className="text-xs text-neutro">El enlace “Editar” de cada fila finaliza esa asignación (le pone fecha de fin hoy).</p>
        </>
      )}

      <SlideOver
        abierto={panel}
        titulo="Asignar recurso a una persona"
        onCerrar={() => setPanel(false)}
        footer={
          <div className="flex justify-end gap-2">
            <Button variant="texto" onClick={() => setPanel(false)}>Cancelar</Button>
            <Button variant="primario" onClick={guardar}>Asignar</Button>
          </div>
        }
      >
        <div className="space-y-4">
          <SelectField
            label="Persona"
            required
            options={(personas.data ?? []).map((p) => ({ value: p.id, label: `${p.nombre} ${p.apellido}` }))}
            value={valores.persona_id}
            error={errores.persona_id}
            onChange={(e) => setValor("persona_id", e.target.value)}
          />
          <SelectField
            label="Tipo de recurso"
            required
            options={TIPOS}
            value={valores.tipo_recurso}
            error={errores.tipo_recurso}
            onChange={(e) => { setValor("tipo_recurso", e.target.value); setValor("recurso_id", ""); }}
          />
          <SelectField
            label="Recurso"
            required
            options={opcionesRecurso}
            value={valores.recurso_id}
            error={errores.recurso_id}
            onChange={(e) => setValor("recurso_id", e.target.value)}
          />
          <TextField
            label="Fecha de inicio"
            type="date"
            dato
            value={valores.fecha_inicio}
            error={errores.fecha_inicio}
            onChange={(e) => setValor("fecha_inicio", e.target.value)}
          />
          <TextAreaField
            label="Observaciones"
            maxLength={500}
            value={valores.observaciones ?? ""}
            error={errores.observaciones}
            onChange={(e) => setValor("observaciones", e.target.value)}
          />
        </div>
      </SlideOver>
    </div>
  );
}
