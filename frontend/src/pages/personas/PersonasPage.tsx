import { useMemo, useState } from "react";
import { useSearchParams } from "react-router-dom";
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
import { useAsignacionesPorPersona, useCrudMutations, useDepartamentos, usePersonas } from "../../lib/queries";
import type { Persona } from "../../lib/types";
import { formatFecha } from "../../lib/formatters";

const REGLAS: ReglaCampo[] = [
  { name: "nombre", label: "Nombre", tipo: "text", required: true, max: 100 },
  { name: "apellido", label: "Apellido", tipo: "text", required: true, max: 100 },
  { name: "documento", label: "Documento", tipo: "numero", min: 6, max: 11 },
  { name: "email", label: "Email", tipo: "email" },
  { name: "telefono", label: "Teléfono", tipo: "telefono", max: 20 },
  { name: "departamento_id", label: "Departamento", tipo: "select" },
];

export function PersonasPage() {
  const [params] = useSearchParams();
  const filtro = (params.get("q") ?? "").toLowerCase();

  const personas = usePersonas();
  const departamentos = useDepartamentos();
  const { crear, actualizar, eliminar } = useCrudMutations<Persona>("personas", "/personas");
  const { mostrar } = useToast();
  const { valores, errores, setValor, setValoresDesde, validarTodos, validarUno } = useFormulario(REGLAS);

  const [panel, setPanel] = useState<{ modo: "crear" | "editar"; item: Persona | null } | null>(null);
  const [verDetalle, setVerDetalle] = useState<Persona | null>(null);
  const [aBorrar, setABorrar] = useState<Persona | null>(null);

  const asignaciones = useAsignacionesPorPersona(verDetalle?.id ?? null);

  const nombreDepto = (id: number | null) => departamentos.data?.find((d) => d.id === id)?.nombre ?? "—";

  const items = useMemo(() => {
    const lista = personas.data ?? [];
    if (!filtro) return lista;
    return lista.filter((p) => `${p.nombre} ${p.apellido} ${p.documento ?? ""}`.toLowerCase().includes(filtro));
  }, [personas.data, filtro]);

  const columnas: ColumnDef<Persona, any>[] = [
    { header: "Nombre", accessorFn: (p) => `${p.nombre} ${p.apellido}` },
    { header: "Documento", accessorKey: "documento", cell: (c) => <span className="dato">{c.getValue() ?? "—"}</span> },
    { header: "Departamento", accessorKey: "departamento_id", cell: (c) => nombreDepto(c.getValue()) },
    { header: "Contacto", accessorKey: "email", cell: (c) => c.getValue() ?? "—" },
  ];

  function abrirCrear() {
    setValoresDesde(null);
    setPanel({ modo: "crear", item: null });
  }

  function abrirEditar(p: Persona) {
    setValoresDesde(p);
    setPanel({ modo: "editar", item: p });
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
        mostrar("Persona creada.");
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
      mostrar("Persona eliminada.");
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo eliminar.", "error");
    } finally {
      setABorrar(null);
    }
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Personas</h1>
        <Button variant="primario" onClick={abrirCrear}>
          Crear
        </Button>
      </div>

      {personas.isLoading && <EmptyState titulo="Cargando…" />}
      {personas.isError && (
        <ErrorState mensaje={(personas.error as Error)?.message ?? ""} onReintentar={() => personas.refetch()} />
      )}
      {!personas.isLoading && !personas.isError && (
        <DataTable
          columns={columnas}
          data={items}
          onVer={setVerDetalle}
          onEditar={abrirEditar}
          vacioTitulo={filtro ? "Ningún resultado para esta búsqueda." : "Todavía no hay personas cargadas."}
        />
      )}

      {/* Panel de detalle: recursos asignados */}
      <SlideOver abierto={verDetalle !== null} titulo={verDetalle ? `${verDetalle.nombre} ${verDetalle.apellido}` : ""} onCerrar={() => setVerDetalle(null)}>
        {verDetalle && (
          <div className="space-y-5">
            <div>
              <p className="text-sm font-medium text-tinta">Datos generales</p>
              <dl className="mt-2 space-y-1 text-sm">
                <div className="flex justify-between"><dt className="text-neutro">Documento</dt><dd className="dato">{verDetalle.documento ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Departamento</dt><dd>{nombreDepto(verDetalle.departamento_id)}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Email</dt><dd>{verDetalle.email ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Teléfono</dt><dd className="dato">{verDetalle.telefono ?? "—"}</dd></div>
              </dl>
            </div>
            <div>
              <p className="text-sm font-medium text-tinta">Recursos asignados</p>
              {asignaciones.isLoading && <p className="mt-2 text-sm text-neutro">Cargando…</p>}
              {!asignaciones.isLoading && (asignaciones.data ?? []).length === 0 && (
                <p className="mt-2 text-sm text-neutro">No tiene recursos asignados.</p>
              )}
              {(asignaciones.data ?? []).length > 0 && (
                <ul className="mt-2 divide-y divide-filete border border-filete">
                  {asignaciones.data!.map((a) => (
                    <li key={a.id} className="flex items-center justify-between px-3 py-2 text-sm">
                      <div>
                        <p className="capitalize text-tinta">{a.tipo_recurso}</p>
                        <p className="dato text-neutro">desde {formatFecha(a.fecha_inicio)}</p>
                      </div>
                      <span className={a.fecha_fin ? "text-neutro" : "text-linea-ok"}>
                        {a.fecha_fin ? "Finalizada" : "Activa"}
                      </span>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </div>
        )}
      </SlideOver>

      {/* Panel de alta/edición */}
      <SlideOver
        abierto={panel !== null}
        titulo={panel?.modo === "crear" ? "Crear persona" : "Editar persona"}
        onCerrar={() => setPanel(null)}
        footer={
          <div className="flex items-center justify-between">
            {panel?.modo === "editar" && panel.item && (
              <Button variant="destructivo" onClick={() => { setABorrar(panel.item); setPanel(null); }}>
                Eliminar
              </Button>
            )}
            <div className="ml-auto flex gap-2">
              <Button variant="texto" onClick={() => setPanel(null)}>Cancelar</Button>
              <Button variant="primario" onClick={guardar} disabled={crear.isPending || actualizar.isPending}>
                Guardar cambios
              </Button>
            </div>
          </div>
        }
      >
        <div className="space-y-4">
          <TextField label="Nombre" required maxLength={100} value={valores.nombre ?? ""} error={errores.nombre} onChange={(e) => setValor("nombre", e.target.value)} onBlur={() => validarUno("nombre")} />
          <TextField label="Apellido" required maxLength={100} value={valores.apellido ?? ""} error={errores.apellido} onChange={(e) => setValor("apellido", e.target.value)} onBlur={() => validarUno("apellido")} />
          <TextField label="Documento" dato inputMode="numeric" maxLength={11} value={valores.documento ?? ""} error={errores.documento} onChange={(e) => setValor("documento", e.target.value)} onBlur={() => validarUno("documento")} />
          <TextField label="Email" type="email" value={valores.email ?? ""} error={errores.email} onChange={(e) => setValor("email", e.target.value)} onBlur={() => validarUno("email")} />
          <TextField label="Teléfono" dato inputMode="tel" maxLength={20} value={valores.telefono ?? ""} error={errores.telefono} onChange={(e) => setValor("telefono", e.target.value)} onBlur={() => validarUno("telefono")} />
          <SelectField
            label="Departamento"
            options={(departamentos.data ?? []).map((d) => ({ value: d.id, label: d.nombre }))}
            value={valores.departamento_id ?? ""}
            error={errores.departamento_id}
            onChange={(e) => setValor("departamento_id", e.target.value)}
          />
        </div>
      </SlideOver>

      <ConfirmDialog
        abierto={aBorrar !== null}
        titulo="Eliminar persona"
        descripcion={aBorrar ? `Se va a eliminar a ${aBorrar.nombre} ${aBorrar.apellido}. Esta acción no se puede deshacer.` : ""}
        onConfirmar={confirmarBorrado}
        onCancelar={() => setABorrar(null)}
      />
    </div>
  );
}