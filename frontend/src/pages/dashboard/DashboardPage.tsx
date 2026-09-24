import type { ReactNode } from "react";
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
import { Button } from "../../components/ui/Button";

function Conteo({ valor, etiqueta }: { valor: number | undefined; etiqueta: string }) {
  return (
    <div className="border-l border-filete px-6 py-5 text-center first:border-l-0">
      <p className="dato text-3xl font-bold text-senal">{valor ?? "—"}</p>
      <p className="mt-1 text-sm text-neutro">{etiqueta}</p>
    </div>
  );
}

function Tarjeta({ titulo, accion, children }: { titulo: string; accion?: string; children: ReactNode }) {
  return (
    <div className="flex flex-col border border-filete border-t-4 border-t-senal bg-papel-alto">
      <div className="flex items-center justify-between gap-2 border-b border-filete px-4 py-3">
        <h2 className="text-sm font-bold text-tinta">{titulo}</h2>
        {accion && <a className="text-xs font-semibold text-senal hover:underline">{accion} →</a>}
      </div>
      {children}
    </div>
  );
}

function DiasPill({ dias }: { dias: number }) {
  const clase =
    dias <= 15
      ? "bg-[#fbefee] text-linea-baja"
      : dias <= 45
        ? "bg-[#faf2e3] text-aviso"
        : "bg-verde-suave text-senal";
  return (
    <span className={`inline-flex shrink-0 items-center rounded-full px-2.5 py-1 text-xs font-bold ${clase}`}>
      {dias} días
    </span>
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
    <div className="space-y-6">
      <div className="flex flex-wrap items-end justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-tinta">Panel de control</h1>
          <p className="mt-0.5 text-xs text-neutro">
            Inventario de telefonía · <span className="font-semibold text-senal">Resumen general</span>
          </p>
        </div>
        <Button variant="secundario">Exportar reporte</Button>
      </div>

      <section className="grid grid-cols-2 border border-filete bg-papel-alto sm:grid-cols-3 lg:grid-cols-5">
        <Conteo valor={inventario.data?.sims} etiqueta="SIMs" />
        <Conteo valor={inventario.data?.telefonos_fijos} etiqueta="teléfonos fijos" />
        <Conteo valor={inventario.data?.dispositivos} etiqueta="dispositivos" />
        <Conteo valor={extensiones.data?.length} etiqueta="extensiones" />
        <Conteo valor={inventario.data?.personas} etiqueta="personas" />
      </section>

      <div className="grid gap-6 lg:grid-cols-3">
        <Tarjeta titulo="Vencimientos próximos" accion="Ver todos">
          {vencimientos.length === 0 ? (
            <EmptyState titulo="No hay contratos por vencer en los próximos 60 días." />
          ) : (
            <ul className="flex-1 divide-y divide-filete">
              {vencimientos.map((c) => (
                <li key={c.id} className="flex items-center justify-between gap-3 px-4 py-3 text-sm">
                  <div>
                    <p className="font-semibold text-tinta">Contrato {c.numero}</p>
                    <p className="dato text-xs text-neutro">{formatFecha(c.fecha_vencimiento)}</p>
                  </div>
                  {c.dias !== null && <DiasPill dias={c.dias} />}
                </li>
              ))}
            </ul>
          )}
        </Tarjeta>

        <Tarjeta titulo="Consumo del período" accion="Detalle">
          {!ultimoPeriodo ? (
            <EmptyState titulo="Todavía no se importó ninguna factura de consumo." />
          ) : (
            <ul className="flex-1 divide-y divide-filete">
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
                <span className="dato font-bold text-senal">{formatMoneda(ultimoPeriodo.consumo)}</span>
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
        </Tarjeta>

        <Tarjeta titulo="Recursos sin asignar" accion="Gestionar">
          {recursosSueltos.length === 0 ? (
            <EmptyState titulo="No hay recursos sin asignar." />
          ) : (
            <ul className="flex-1 divide-y divide-filete">
              {recursosSueltos.slice(0, 6).map((r) => (
                <li key={`${r.tipo}-${r.id}`} className="flex items-center justify-between gap-3 px-4 py-3 text-sm">
                  <span className="text-tinta">{r.descripcion}</span>
                  <span className="shrink-0 rounded-full border border-filete bg-papel px-2 py-0.5 text-xs text-neutro">
                    {r.tipo}
                  </span>
                </li>
              ))}
            </ul>
          )}
        </Tarjeta>
      </div>

      <div className="grid gap-6 lg:grid-cols-2">
        <Tarjeta titulo="Últimas facturas importadas">
          {(facturas.data ?? []).length === 0 ? (
            <EmptyState titulo="No hay facturas importadas todavía." />
          ) : (
            <ul className="flex-1 divide-y divide-filete">
              {(facturas.data ?? []).slice(0, 6).map((f) => (
                <li key={f.id} className="flex items-center justify-between gap-3 px-4 py-3 text-sm">
                  <div>
                    <p className="dato font-semibold text-tinta">{f.no_factura}</p>
                    <p className="text-xs text-neutro">{formatFecha(f.fecha_vencimiento)}</p>
                  </div>
                  <span className="dato font-bold text-tinta">{formatMoneda(f.total_a_pagar)}</span>
                </li>
              ))}
            </ul>
          )}
        </Tarjeta>

        <Tarjeta titulo="Inventario">
          {!inventario.data ? (
            <EmptyState titulo="Sin información de inventario." />
          ) : (
            <ul className="flex-1 divide-y divide-filete">
              <li className="flex items-center justify-between px-4 py-3 text-sm">
                <span className="text-tinta">Personas</span>
                <span className="dato font-bold text-senal">{inventario.data.personas}</span>
              </li>
              <li className="flex items-center justify-between px-4 py-3 text-sm">
                <span className="text-tinta">Placas SIM</span>
                <span className="dato font-bold text-senal">{inventario.data.sims}</span>
              </li>
              <li className="flex items-center justify-between px-4 py-3 text-sm">
                <span className="text-tinta">Teléfonos fijos</span>
                <span className="dato font-bold text-senal">{inventario.data.telefonos_fijos}</span>
              </li>
              <li className="flex items-center justify-between px-4 py-3 text-sm">
                <span className="text-tinta">Dispositivos</span>
                <span className="dato font-bold text-senal">{inventario.data.dispositivos}</span>
              </li>
            </ul>
          )}
        </Tarjeta>
      </div>
    </div>
  );
}