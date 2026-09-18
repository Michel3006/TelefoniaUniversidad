import { useState } from "react";
import { Button } from "../../components/ui/Button";
import { TextAreaField } from "../../components/ui/Field";
import { useToast } from "../../components/ui/Toast";
import { ApiError } from "../../lib/api";
import { useImportarRrhh, useSincronizarRrhh } from "../../lib/queries";
import type { SincronizacionResumen } from "../../lib/types";

function Resumen({ resumen }: { resumen: SincronizacionResumen | null }) {
  const filas = [
    { label: "cargos", valor: resumen?.cargos },
    { label: "áreas", valor: resumen?.areas },
    { label: "unidades organizativas", valor: resumen?.unidades },
    { label: "empleados", valor: resumen?.empleados },
  ];
  return (
    <div className="flex flex-wrap gap-6 border border-filete bg-papel-alto px-6 py-5">
      {filas.map((f) => (
        <div key={f.label} className="border-l border-filete px-6 first:border-l-0 first:pl-0">
          <p className="dato text-2xl font-bold text-tinta">{f.valor ?? "—"}</p>
          <p className="mt-1 text-sm text-neutro">{f.label} procesados</p>
        </div>
      ))}
    </div>
  );
}

export function SincronizacionPage() {
  const [resumen, setResumen] = useState<SincronizacionResumen | null>(null);
  const [json, setJson] = useState("");
  const sincronizar = useSincronizarRrhh();
  const importar = useImportarRrhh();
  const { mostrar } = useToast();

  async function ejecutarSincronizacion() {
    try {
      const r = await sincronizar.mutateAsync();
      setResumen(r);
      mostrar("Sincronización completada.");
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo sincronizar.", "error");
    }
  }

  async function importarJson() {
    let payload: Record<string, unknown>;
    try {
      payload = JSON.parse(json) as Record<string, unknown>;
    } catch {
      mostrar("El texto no es un JSON válido.", "error");
      return;
    }
    try {
      const r = await importar.mutateAsync(payload);
      setResumen(r);
      mostrar("Importación completada.");
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo importar.", "error");
    }
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Sincronización RRHH</h1>
      </div>

      <div className="border border-filete bg-papel-alto px-4 py-3 text-sm text-neutro">
        Copia trabajadores, unidades organizativas, cargos y áreas desde el sistema institucional ASSETS_RH hacia
        las tablas locales de espejo. Personas y departamentos son de solo lectura y se actualizan desde aquí.
      </div>

      <section className="space-y-3 border border-filete bg-papel-alto p-4">
        <h2 className="text-sm font-semibold text-tinta">Sincronización directa (SQL Server)</h2>
        <p className="text-sm text-neutro">
          Requiere que el backend tenga habilitada la conexión (ASSETS_RRH_HABILITADO=true y credenciales en el .env).
        </p>
        <Button variant="primario" onClick={ejecutarSincronizacion} disabled={sincronizar.isPending}>
          {sincronizar.isPending ? "Sincronizando…" : "Sincronizar desde ASSETS_RH"}
        </Button>
      </section>

      <section className="space-y-3 border border-filete bg-papel-alto p-4">
        <h2 className="text-sm font-semibold text-tinta">Importación desde JSON</h2>
        <p className="text-sm text-neutro">
          Fallback para cuando no hay conexión directa. JSON con claves{" "}
          <span className="dato">cargos</span>, <span className="dato">areas</span>,{" "}
          <span className="dato">unidades</span> y <span className="dato">empleados</span> (cada una una lista).
        </p>
        <TextAreaField
          label="JSON"
          value={json}
          onChange={(e) => setJson(e.target.value)}
          placeholder={'{\n  "cargos": [{ "codigo": "001", "nombre": "Rector" }],\n  "areas": [],\n  "unidades": [],\n  "empleados": []\n}'}
        />
        <Button variant="primario" onClick={importarJson} disabled={importar.isPending}>
          {importar.isPending ? "Importando…" : "Importar desde JSON"}
        </Button>
      </section>

      <Resumen resumen={resumen} />
    </div>
  );
}