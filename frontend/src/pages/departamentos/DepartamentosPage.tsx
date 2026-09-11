import { useState } from "react";
import { Button } from "../../components/ui/Button";
import { SlideOver } from "../../components/ui/SlideOver";
import { ConfirmDialog } from "../../components/ui/ConfirmDialog";
import { TextField, SelectField } from "../../components/ui/Field";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { useToast } from "../../components/ui/Toast";
import { ApiError } from "../../lib/api";
import { useFormulario } from "../../lib/useFormulario";
import { toPayload, type ReglaCampo } from "../../lib/validation";
import { useCrudMutations, useDepartamentos } from "../../lib/queries";
import type { Departamento } from "../../lib/types";

const REGLAS: ReglaCampo[] = [
  { name: "nombre", label: "Nombre", tipo: "text", required: true, max: 150 },
  { name: "departamento_padre_id", label: "Departamento padre", tipo: "select" },
];

function construirArbol(deptos: Departamento[]) {
  const hijosDe = (padreId: number | null) => deptos.filter((d) => d.departamento_padre_id === padreId);

  function render(padreId: number | null, nivel: number, onEditar: (d: Departamento) => void): JSX.Element[] {
    return hijosDe(padreId).flatMap((d) => [
      <div
        key={d.id}
        className="group flex items-center justify-between border-b border-filete py-2 pr-3 text-sm"
        style={{ paddingLeft: `${nivel * 20 + 4}px` }}
      >
        <span className="text-tinta">{d.nombre}</span>
        <button
          onClick={() => onEditar(d)}
          className="invisible font-medium text-tinta underline-offset-2 group-hover:visible hover:underline"
        >
          Editar
        </button>
      </div>,
      ...render(d.id, nivel + 1, onEditar),
    ]);
  }

  return render;
}

export function DepartamentosPage() {
  const departamentos = useDepartamentos();
  const { crear, actualizar, eliminar } = useCrudMutations<Departamento>("departamentos", "/departamentos");
  const { mostrar } = useToast();

  const [panel, setPanel] = useState<{ modo: "crear" | "editar"; item: Departamento | null } | null>(null);
  const [aBorrar, setABorrar] = useState<Departamento | null>(null);
  const { valores, errores, setValor, setValoresDesde, validarTodos, validarUno } = useFormulario(REGLAS);

  function abrirCrear() {
    setValoresDesde(null);
    setPanel({ modo: "crear", item: null });
  }

  function abrirEditar(d: Departamento) {
    setValoresDesde(d);
    setPanel({ modo: "editar", item: d });
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
        mostrar("Departamento creado.");
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
      mostrar("Departamento eliminado.");
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo eliminar. Verificá que no tenga subordinados.", "error");
    } finally {
      setABorrar(null);
    }
  }

  const items = departamentos.data ?? [];
  const render = construirArbol(items);

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Departamentos</h1>
        <Button variant="primario" onClick={abrirCrear}>Crear</Button>
      </div>

      {departamentos.isLoading && <EmptyState titulo="Cargando…" />}
      {departamentos.isError && (
        <ErrorState mensaje={(departamentos.error as Error)?.message ?? ""} onReintentar={() => departamentos.refetch()} />
      )}
      {!departamentos.isLoading && !departamentos.isError && items.length === 0 && (
        <EmptyState titulo="Todavía no hay departamentos cargados." />
      )}
      {!departamentos.isLoading && !departamentos.isError && items.length > 0 && (
        <div className="border border-filete bg-papel-alto px-3">{render(null, 0, abrirEditar)}</div>
      )}

      <SlideOver
        abierto={panel !== null}
        titulo={panel?.modo === "crear" ? "Crear departamento" : "Editar departamento"}
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
          <TextField
            label="Nombre"
            required
            maxLength={150}
            value={valores.nombre}
            error={errores.nombre}
            onChange={(e) => setValor("nombre", e.target.value)}
            onBlur={() => validarUno("nombre")}
          />
          <SelectField
            label="Departamento padre"
            hint="Dejalo vacío si es un departamento raíz."
            options={items.filter((d) => d.id !== panel?.item?.id).map((d) => ({ value: d.id, label: d.nombre }))}
            value={valores.departamento_padre_id}
            error={errores.departamento_padre_id}
            onChange={(e) => setValor("departamento_padre_id", e.target.value)}
          />
        </div>
      </SlideOver>

      <ConfirmDialog
        abierto={aBorrar !== null}
        titulo="Eliminar departamento"
        descripcion={aBorrar ? `Se va a eliminar "${aBorrar.nombre}". Esta acción no se puede deshacer.` : ""}
        onConfirmar={confirmarBorrado}
        onCancelar={() => setABorrar(null)}
      />
    </div>
  );
}
