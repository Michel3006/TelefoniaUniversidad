import { useMemo, useState } from "react";
import { Button } from "../../components/ui/Button";
import { SlideOver } from "../../components/ui/SlideOver";
import { ConfirmDialog } from "../../components/ui/ConfirmDialog";
import { TextField, TextAreaField, SelectField } from "../../components/ui/Field";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { useToast } from "../../components/ui/Toast";
import { ApiError } from "../../lib/api";
import { useFormulario } from "../../lib/useFormulario";
import { toPayload, type ReglaCampo } from "../../lib/validation";
import { useCrudMutations, useEdificios, useLocales } from "../../lib/queries";
import type { Edificio, Local } from "../../lib/types";

const REGLAS_LOCAL: ReglaCampo[] = [
  { name: "edificio_id", label: "Edificio", tipo: "select", required: true },
  { name: "piso", label: "Piso", tipo: "text", max: 50 },
  { name: "oficina", label: "Oficina", tipo: "text", max: 50 },
  { name: "descripcion", label: "Descripción", tipo: "textarea", max: 250 },
];

const REGLAS_EDIFICIO: ReglaCampo[] = [
  { name: "nombre", label: "Nombre", tipo: "text", required: true, max: 150 },
  { name: "direccion", label: "Dirección", tipo: "text", max: 250 },
];

export function LocalesPage() {
  const edificios = useEdificios();
  const locales = useLocales();
  const localesCrud = useCrudMutations<Local>("locales", "/locales");
  const edificiosCrud = useCrudMutations<Edificio>("edificios", "/edificios");
  const { mostrar } = useToast();

  const localForm = useFormulario(REGLAS_LOCAL);
  const edificioForm = useFormulario(REGLAS_EDIFICIO);

  const [panelLocal, setPanelLocal] = useState<{ modo: "crear" | "editar"; item: Local | null; edificioId?: number } | null>(null);
  const [panelEdificio, setPanelEdificio] = useState<{ modo: "crear" | "editar"; item: Edificio | null } | null>(null);
  const [aBorrar, setABorrar] = useState<Local | null>(null);

  const porEdificio = useMemo(() => {
    const mapa = new Map<number, Local[]>();
    for (const l of locales.data ?? []) {
      if (!mapa.has(l.edificio_id)) mapa.set(l.edificio_id, []);
      mapa.get(l.edificio_id)!.push(l);
    }
    return mapa;
  }, [locales.data]);

  function abrirCrearLocal(edificioId: number) {
    localForm.setValores({ edificio_id: String(edificioId), piso: "", oficina: "", descripcion: "" });
    setPanelLocal({ modo: "crear", item: null, edificioId });
  }

  function abrirEditarLocal(l: Local) {
    localForm.setValoresDesde(l);
    setPanelLocal({ modo: "editar", item: l });
  }

  async function guardarLocal() {
    if (!localForm.validarTodos()) {
      mostrar("Revisá los campos marcados en rojo.", "error");
      return;
    }
    const payload = toPayload(REGLAS_LOCAL, localForm.valores);
    try {
      if (panelLocal?.modo === "crear") {
        await localesCrud.crear.mutateAsync(payload);
        mostrar("Local creado.");
      } else if (panelLocal?.item) {
        await localesCrud.actualizar.mutateAsync({ id: panelLocal.item.id, payload });
        mostrar("Cambios guardados.");
      }
      setPanelLocal(null);
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo guardar.", "error");
    }
  }

  async function confirmarBorrado() {
    if (!aBorrar) return;
    try {
      await localesCrud.eliminar.mutateAsync(aBorrar.id);
      mostrar("Local eliminado.");
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo eliminar.", "error");
    } finally {
      setABorrar(null);
    }
  }

  function abrirCrearEdificio() {
    edificioForm.setValoresDesde(null);
    setPanelEdificio({ modo: "crear", item: null });
  }

  function abrirEditarEdificio(e: Edificio) {
    edificioForm.setValoresDesde(e);
    setPanelEdificio({ modo: "editar", item: e });
  }

  async function guardarEdificio() {
    if (!edificioForm.validarTodos()) {
      mostrar("Revisá los campos marcados en rojo.", "error");
      return;
    }
    const payload = toPayload(REGLAS_EDIFICIO, edificioForm.valores);
    try {
      if (panelEdificio?.modo === "crear") {
        await edificiosCrud.crear.mutateAsync(payload);
        mostrar("Edificio creado.");
      } else if (panelEdificio?.item) {
        await edificiosCrud.actualizar.mutateAsync({ id: panelEdificio.item.id, payload });
        mostrar("Cambios guardados.");
      }
      setPanelEdificio(null);
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo guardar.", "error");
    }
  }

  if (edificios.isLoading || locales.isLoading) return <EmptyState titulo="Cargando…" />;
  if (edificios.isError) return <ErrorState mensaje={(edificios.error as Error)?.message ?? ""} onReintentar={() => edificios.refetch()} />;
  if (locales.isError) return <ErrorState mensaje={(locales.error as Error)?.message ?? ""} onReintentar={() => locales.refetch()} />;

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Locales</h1>
        <Button variant="secundario" onClick={abrirCrearEdificio}>Crear edificio</Button>
      </div>

      {(edificios.data ?? []).length === 0 && (
        <EmptyState titulo="Todavía no hay edificios cargados." descripcion="Creá un edificio para poder agregar locales dentro." />
      )}

      {(edificios.data ?? []).map((edificio) => (
        <section key={edificio.id} className="border border-filete bg-papel-alto">
          <div className="flex items-center justify-between border-b border-filete px-4 py-3">
            <div>
              <p className="text-sm font-semibold text-tinta">{edificio.nombre}</p>
              {edificio.direccion && <p className="text-xs text-neutro">{edificio.direccion}</p>}
            </div>
            <div className="flex gap-3 text-sm">
              <button onClick={() => abrirEditarEdificio(edificio)} className="font-medium text-tinta underline-offset-2 hover:underline">
                Editar edificio
              </button>
              <button onClick={() => abrirCrearLocal(edificio.id)} className="font-medium text-senal underline-offset-2 hover:underline">
                Agregar local
              </button>
            </div>
          </div>
          {(porEdificio.get(edificio.id) ?? []).length === 0 ? (
            <p className="px-4 py-4 text-sm text-neutro">Sin locales cargados en este edificio.</p>
          ) : (
            <table className="w-full text-left text-sm">
              <thead>
                <tr className="border-b border-filete text-[13px] font-semibold text-tinta">
                  <th className="px-4 py-2">Piso</th>
                  <th className="px-4 py-2">Oficina</th>
                  <th className="px-4 py-2">Descripción</th>
                  <th className="px-4 py-2" />
                </tr>
              </thead>
              <tbody>
                {(porEdificio.get(edificio.id) ?? []).map((l) => (
                  <tr key={l.id} className="group border-b border-filete last:border-b-0 hover:bg-black/[0.015]">
                    <td className="px-4 py-2.5">{l.piso ?? "—"}</td>
                    <td className="px-4 py-2.5">{l.oficina ?? "—"}</td>
                    <td className="px-4 py-2.5">{l.descripcion ?? "—"}</td>
                    <td className="px-4 py-2.5 text-right">
                      <button
                        onClick={() => abrirEditarLocal(l)}
                        className="invisible font-medium text-tinta underline-offset-2 group-hover:visible hover:underline"
                      >
                        Editar
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </section>
      ))}

      <SlideOver
        abierto={panelLocal !== null}
        titulo={panelLocal?.modo === "crear" ? "Crear local" : "Editar local"}
        onCerrar={() => setPanelLocal(null)}
        footer={
          <div className="flex items-center justify-between">
            {panelLocal?.modo === "editar" && panelLocal.item && (
              <Button variant="destructivo" onClick={() => { setABorrar(panelLocal.item); setPanelLocal(null); }}>
                Eliminar
              </Button>
            )}
            <div className="ml-auto flex gap-2">
              <Button variant="texto" onClick={() => setPanelLocal(null)}>Cancelar</Button>
              <Button variant="primario" onClick={guardarLocal}>Guardar cambios</Button>
            </div>
          </div>
        }
      >
        <div className="space-y-4">
          <SelectField
            label="Edificio"
            required
            options={(edificios.data ?? []).map((e) => ({ value: e.id, label: e.nombre }))}
            value={localForm.valores.edificio_id ?? ""}
            error={localForm.errores.edificio_id}
            onChange={(e) => localForm.setValor("edificio_id", e.target.value)}
          />
          <TextField label="Piso" maxLength={50} value={localForm.valores.piso ?? ""} error={localForm.errores.piso} onChange={(e) => localForm.setValor("piso", e.target.value)} onBlur={() => localForm.validarUno("piso")} />
          <TextField label="Oficina" maxLength={50} value={localForm.valores.oficina ?? ""} error={localForm.errores.oficina} onChange={(e) => localForm.setValor("oficina", e.target.value)} onBlur={() => localForm.validarUno("oficina")} />
          <TextAreaField label="Descripción" maxLength={250} value={localForm.valores.descripcion ?? ""} error={localForm.errores.descripcion} onChange={(e) => localForm.setValor("descripcion", e.target.value)} onBlur={() => localForm.validarUno("descripcion")} />
        </div>
      </SlideOver>

      <SlideOver
        abierto={panelEdificio !== null}
        titulo={panelEdificio?.modo === "crear" ? "Crear edificio" : "Editar edificio"}
        onCerrar={() => setPanelEdificio(null)}
        footer={
          <div className="flex justify-end gap-2">
            <Button variant="texto" onClick={() => setPanelEdificio(null)}>Cancelar</Button>
            <Button variant="primario" onClick={guardarEdificio}>Guardar cambios</Button>
          </div>
        }
      >
        <div className="space-y-4">
          <TextField label="Nombre" required maxLength={150} value={edificioForm.valores.nombre ?? ""} error={edificioForm.errores.nombre} onChange={(e) => edificioForm.setValor("nombre", e.target.value)} onBlur={() => edificioForm.validarUno("nombre")} />
          <TextField label="Dirección" maxLength={250} value={edificioForm.valores.direccion ?? ""} error={edificioForm.errores.direccion} onChange={(e) => edificioForm.setValor("direccion", e.target.value)} onBlur={() => edificioForm.validarUno("direccion")} />
        </div>
      </SlideOver>

      <ConfirmDialog
        abierto={aBorrar !== null}
        titulo="Eliminar local"
        descripcion="Esta acción no se puede deshacer."
        onConfirmar={confirmarBorrado}
        onCancelar={() => setABorrar(null)}
      />
    </div>
  );
}