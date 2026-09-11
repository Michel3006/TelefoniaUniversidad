import { useMemo, useState } from "react";
import type { ColumnDef } from "@tanstack/react-table";
import type { UseQueryResult } from "@tanstack/react-query";
import { DataTable } from "../ui/DataTable";
import { SlideOver } from "../ui/SlideOver";
import { ConfirmDialog } from "../ui/ConfirmDialog";
import { Button } from "../ui/Button";
import { TextField, TextAreaField, SelectField } from "../ui/Field";
import { EmptyState, ErrorState } from "../ui/EmptyState";
import { useCrudMutations } from "../../lib/queries";
import { useToast } from "../ui/Toast";
import { ApiError } from "../../lib/api";
import { useFormulario } from "../../lib/useFormulario";
import { toPayload, type ReglaCampo, type TipoCampo } from "../../lib/validation";

export type TipoCampoTexto = Exclude<TipoCampo, "select" | "textarea">;

interface CampoBase {
  name: string;
  label: string;
  required?: boolean;
  placeholder?: string;
  min?: number;
  max?: number;
}

export type CampoConfig =
  | (CampoBase & {
      type: TipoCampoTexto;
      dato?: boolean;
    })
  | (CampoBase & { type: "textarea" })
  | (CampoBase & { type: "select"; options?: { value: number | string; label: string }[] });

function aReglas(campos: CampoConfig[]): ReglaCampo[] {
  return campos.map((c) => ({
    name: c.name,
    label: c.label,
    tipo: c.type,
    required: c.required,
    min: c.min,
    max: c.max,
  }));
}

function inputAttrs(campo: Extract<CampoConfig, { type: TipoCampoTexto }>) {
  switch (campo.type) {
    case "email":
      return { type: "email" as const, inputMode: "email" as const };
    case "date":
      return { type: "date" as const };
    case "decimal":
      return { type: "text" as const, inputMode: "decimal" as const };
    case "numero":
    case "cuit":
      return { type: "text" as const, inputMode: "numeric" as const };
    case "telefono":
      return { type: "text" as const, inputMode: "tel" as const };
    case "password":
      return { type: "password" as const };
    default:
      return { type: "text" as const };
  }
}

interface CrudPageProps<T extends { id: number }> {
  titulo: string;
  descripcionVacio?: string;
  entidadKey: string;
  basePath: string;
  useLista: () => UseQueryResult<T[], Error>;
  columnas: ColumnDef<T, any>[];
  campos: CampoConfig[];
  nombreItem: (item: T) => string;
  accionesExtra?: React.ReactNode;
}

export function CrudPage<T extends { id: number }>({
  titulo,
  descripcionVacio,
  entidadKey,
  basePath,
  useLista,
  columnas,
  campos,
  nombreItem,
  accionesExtra,
}: CrudPageProps<T>) {
  const { data, isLoading, isError, error, refetch } = useLista();
  const { crear, actualizar, eliminar } = useCrudMutations<T>(entidadKey, basePath);
  const { mostrar } = useToast();

  const camposMemo = useMemo(() => campos, [campos]);
  const reglas = useMemo(() => aReglas(camposMemo), [camposMemo]);
  const { valores, errores, setValor, setValoresDesde, validarTodos, validarUno } = useFormulario(reglas);

  const [panel, setPanel] = useState<{ modo: "crear" | "editar"; item: T | null } | null>(null);
  const [aBorrar, setABorrar] = useState<T | null>(null);

  const items = useMemo(() => data ?? [], [data]);

  function abrirCrear() {
    setValoresDesde(null);
    setPanel({ modo: "crear", item: null });
  }

  function abrirEditar(item: T) {
    setValoresDesde(item as Record<string, unknown>);
    setPanel({ modo: "editar", item });
  }

  async function guardar() {
    if (!validarTodos()) {
      mostrar("Revisá los campos marcados en rojo.", "error");
      return;
    }
    const payload = toPayload(reglas, valores);
    try {
      if (panel?.modo === "crear") {
        await crear.mutateAsync(payload);
        mostrar("Se creó correctamente.");
      } else if (panel?.item) {
        await actualizar.mutateAsync({ id: panel.item.id, payload });
        mostrar("Se guardaron los cambios.");
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
      mostrar("Se eliminó correctamente.");
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo eliminar.", "error");
    } finally {
      setABorrar(null);
    }
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">{titulo}</h1>
        <div className="flex gap-2">
          {accionesExtra}
          <Button variant="primario" onClick={abrirCrear}>
            Crear
          </Button>
        </div>
      </div>

      {isLoading && <EmptyState titulo="Cargando…" />}
      {isError && <ErrorState mensaje={(error as Error)?.message ?? ""} onReintentar={() => refetch()} />}
      {!isLoading && !isError && (
        <DataTable
          columns={columnas}
          data={items}
          onEditar={abrirEditar}
          vacioTitulo={`Todavía no hay ${titulo.toLowerCase()} cargados.`}
          vacioDescripcion={descripcionVacio}
        />
      )}

      <SlideOver
        abierto={panel !== null}
        titulo={panel?.modo === "crear" ? `Crear ${titulo.toLowerCase().replace(/s$/, "")}` : "Editar"}
        onCerrar={() => setPanel(null)}
        footer={
          <div className="flex items-center justify-between">
            {panel?.modo === "editar" && panel.item && (
              <Button
                variant="destructivo"
                onClick={() => {
                  setABorrar(panel.item);
                  setPanel(null);
                }}
              >
                Eliminar
              </Button>
            )}
            <div className="ml-auto flex gap-2">
              <Button variant="texto" onClick={() => setPanel(null)}>
                Cancelar
              </Button>
              <Button variant="primario" onClick={guardar} disabled={crear.isPending || actualizar.isPending}>
                Guardar cambios
              </Button>
            </div>
          </div>
        }
      >
        <div className="space-y-4">
          {camposMemo.map((c) =>
            c.type === "select" ? (
              <SelectField
                key={c.name}
                label={c.label}
                options={c.options ?? []}
                required={c.required}
                placeholder={c.placeholder}
                value={valores[c.name] ?? ""}
                error={errores[c.name]}
                onChange={(e) => setValor(c.name, e.target.value)}
                onBlur={() => validarUno(c.name)}
              />
            ) : c.type === "textarea" ? (
              <TextAreaField
                key={c.name}
                label={c.label}
                required={c.required}
                value={valores[c.name] ?? ""}
                error={errores[c.name]}
                maxLength={c.max}
                onChange={(e) => setValor(c.name, e.target.value)}
                onBlur={() => validarUno(c.name)}
              />
            ) : (
              <TextField
                key={c.name}
                label={c.label}
                required={c.required}
                dato={c.dato}
                placeholder={c.placeholder}
                maxLength={c.max}
                {...inputAttrs(c)}
                value={valores[c.name] ?? ""}
                error={errores[c.name]}
                onChange={(e) => setValor(c.name, e.target.value)}
                onBlur={() => validarUno(c.name)}
              />
            )
          )}
        </div>
      </SlideOver>

      <ConfirmDialog
        abierto={aBorrar !== null}
        titulo="Eliminar registro"
        descripcion={aBorrar ? `Se va a eliminar "${nombreItem(aBorrar)}". Esta acción no se puede deshacer.` : ""}
        onConfirmar={confirmarBorrado}
        onCancelar={() => setABorrar(null)}
      />
    </div>
  );
}