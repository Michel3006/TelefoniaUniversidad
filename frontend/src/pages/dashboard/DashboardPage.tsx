import {
  useContratos,
  useExtensiones,
  useFacturas,
  useReporteConsumoPorPeriodo,
  useReporteInventario,
  useReporteRecursosSinAsignar,
} from "../../lib/queries";
import { diasHasta, formatFecha, formatMoneda } from "../../lib/formatters";
import { EmptyState } from "../../components/ui/EmptyState";

function Conteo({ valor, etiqueta }: { valor: number | undefined; etiqueta: string }) {
  return (
    <div className="border-l border-filete px-6 py-2 first:border-l-0 first:pl-0">
      <p className="dato text-3xl font-bold text-tinta">{valor ?? "—"}</p>
      <p className="mt-1 text-sm text-neutro">{etiqueta}</p>
    </div>
  );
}

export function DashboardPage() {
  const inventario = useReporteInventario();
  const contratos = useContratos();
  const extensiones = useExtensiones();
  const consumoPorPeriodo = useReporteConsumoPorPeriodo();
  const facturas = useFacturas();
  const recursosSinAsignar = useReporteRecursosSinAsignar();

  const ultimoPeriodo = consumoPorPeriodo.data?.[0];

  const recursosSueltos = recursosSinAsignar.data
    ? [
        ...recursosSinAsignar.data.sims.map((r) => ({ ...r, tipo: "SIM" })),
        ...recursosSinAsignar.data.telefonos.map((r) => ({ ...r, tipo: "Teléfono" })),
        ...recursosSinAsignar.data.dispositivos.map((r) => ({ ...r, tipo: "Dispositivo" })),
        ...recursosSinAsignar.data.extensiones.map((r) => ({ ...r, tipo: "Extensión" })),
      ]
    : [];

  const vencimientos = (contratos.data ?? [])
    .map((c) => ({ ...c, dias: diasHasta(c.fecha_vencimiento) }))
    .filter((c) => c.dias !== null && c.dias <= 60)
    .sort((a, b) => (a.dias ?? 0) - (b.dias ?? 0))
    .slice(0, 6);

  return (
    <div className="space-y-8">
      <section className="flex flex-wrap gap-6 border border-filete bg-papel-alto px-6 py-5">
        <Conteo valor={inventario.data?.sims} etiqueta="SIMs" />
        <Conteo valor={inventario.data?.telefonos_fijos} etiqueta="teléfonos fijos" />
        <Conteo valor={inventario.data?.dispositivos} etiqueta="dispositivos" />
        <Conteo valor={extensiones.data?.length} etiqueta="extensiones" />
        <Conteo valor={inventario.data?.personas} etiqueta="personas" />
      </section>

      <section>
        <h2 className="mb-3 text-sm font-semibold text-tinta">Vencimientos próximos</h2>
        {vencimientos.length === 0 ? (
          <EmptyState titulo="No hay contratos por vencer en los próximos 60 días." />
        ) : (
          <ul className="divide-y divide-filete border border-filete bg-papel-alto">
            {vencimientos.map((c) => (
              <li key={c.id} className="flex items-center justify-between px-4 py-3 text-sm">
                <div>
                  <p className="font-medium text-tinta">Contrato {c.numero}</p>
                  <p className="dato text-neutro">{formatFecha(c.fecha_vencimiento)}</p>
                </div>
                <span className={`text-sm font-medium ${(c.dias ?? 0) <= 15 ? "text-linea-baja" : "text-senal"}`}>
                  {c.dias} días
                </span>
              </li>
            ))}
          </ul>
        )}
      </section>

      <div className="grid gap-6 lg:grid-cols-3">
        <section>
          <h2 className="mb-3 text-sm font-semibold text-tinta">Consumo del período</h2>
          {!ultimoPeriodo ? (
            <EmptyState titulo="Todavía no se importó ninguna factura de consumo." />
          ) : (
            <ul className="divide-y divide-filete border border-filete bg-papel-alto">
              <li className="flex items-center justify-between px-4 py-3 text-sm">
                <span className="text-neutro">Período</span>
                <span className="dato text-tinta">{ultimoPeriodo.periodo}</span>
              </li>
              <li className="flex items-center justify-between px-4 py-3 text-sm">
                <span className="text-neutro">Servicios</span>
                <span className="dato text-tinta">{ultimoPeriodo.registros}</span>
              </li>
              <li className="flex items-center justify-between px-4 py-3 text-sm">
                <span className="text-neutro">Consumo total</span>
                <span className="dato text-tinta">{formatMoneda(ultimoPeriodo.consumo)}</span>
              </li>
              <li className="flex items-center justify-between px-4 py-3 text-sm">
                <span className="text-neutro">Excesos</span>
                <span className="dato text-tinta">{ultimoPeriodo.excesos}</span>
              </li>
              <li className="flex items-center justify-between px-4 py-3 text-sm">
                <span className="text-neutro">Excesos autorizados</span>
                <span className="dato text-tinta">{ultimoPeriodo.excesos_autorizados}</span>
              </li>
              <li className="flex items-center justify-between px-4 py-3 text-sm">
                <span className="text-neutro">Números sin asociar</span>
                <span className="dato text-tinta">{ultimoPeriodo.no_asociados}</span>
              </li>
            </ul>
          )}
        </section>

        <section>
          <h2 className="mb-3 text-sm font-semibold text-tinta">Últimas facturas importadas</h2>
          {(facturas.data ?? []).length === 0 ? (
            <EmptyState titulo="No hay facturas importadas todavía." />
          ) : (
            <ul className="divide-y divide-filete border border-filete bg-papel-alto">
              {(facturas.data ?? []).slice(0, 5).map((f) => (
                <li key={f.id} className="flex items-center justify-between px-4 py-3 text-sm">
                  <div>
                    <p className="dato font-medium text-tinta">{f.no_factura}</p>
                    <p className="text-neutro">{formatFecha(f.fecha_vencimiento)}</p>
                  </div>
                  <span className="dato text-tinta">{formatMoneda(f.total_a_pagar)}</span>
                </li>
              ))}
            </ul>
          )}
        </section>

        <section>
          <h2 className="mb-3 text-sm font-semibold text-tinta">Recursos sin asignar</h2>
          {recursosSueltos.length === 0 ? (
            <EmptyState titulo="No hay recursos sin asignar." />
          ) : (
            <ul className="divide-y divide-filete border border-filete bg-papel-alto">
              {recursosSueltos.slice(0, 6).map((r) => (
                <li key={`${r.tipo}-${r.id}`} className="flex items-center justify-between px-4 py-3 text-sm">
                  <span className="text-tinta">{r.descripcion}</span>
                  <span className="dato text-neutro">{r.tipo}</span>
                </li>
              ))}
            </ul>
          )}
        </section>
      </div>
    </div>
  );
}
