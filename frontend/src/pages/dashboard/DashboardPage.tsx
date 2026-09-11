import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import { useContratos, useDepartamentos, useReporteCostesPorDepartamento, useReporteInventario } from "../../lib/queries";
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
  const departamentos = useDepartamentos();
  const costesPorDepto = useReporteCostesPorDepartamento();

  const nombreDepto = (id: number | null) => departamentos.data?.find((d) => d.id === id)?.nombre ?? "Sin departamento";

  const vencimientos = (contratos.data ?? [])
    .map((c) => ({ ...c, dias: diasHasta(c.fecha_vencimiento) }))
    .filter((c) => c.dias !== null && c.dias <= 60)
    .sort((a, b) => (a.dias ?? 0) - (b.dias ?? 0))
    .slice(0, 6);

  const datosGrafico = (costesPorDepto.data ?? []).map((c) => ({
    nombre: nombreDepto(c.departamento_id),
    total: Number(c.total),
  }));

  return (
    <div className="space-y-8">
      <section className="flex flex-wrap gap-6 border border-filete bg-papel-alto px-6 py-5">
        <Conteo valor={inventario.data?.lineas_moviles} etiqueta="líneas móviles" />
        <Conteo valor={inventario.data?.telefonos_fijos} etiqueta="teléfonos fijos" />
        <Conteo valor={inventario.data?.dispositivos} etiqueta="dispositivos" />
        <Conteo valor={inventario.data?.personas} etiqueta="personas" />
        <Conteo valor={inventario.data?.edificios} etiqueta="edificios" />
        <Conteo valor={inventario.data?.locales} etiqueta="locales" />
      </section>

      <div className="grid gap-6 lg:grid-cols-2">
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

        <section>
          <h2 className="mb-3 text-sm font-semibold text-tinta">Costes por departamento</h2>
          {datosGrafico.length === 0 ? (
            <EmptyState titulo="Todavía no hay costes cargados." />
          ) : (
            <div className="h-64 border border-filete bg-papel-alto p-4">
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={datosGrafico}>
                  <CartesianGrid vertical={false} stroke="#D8DAD4" />
                  <XAxis dataKey="nombre" tick={{ fontSize: 12, fill: "#1C1F1D" }} axisLine={{ stroke: "#D8DAD4" }} />
                  <YAxis tick={{ fontSize: 12, fill: "#8B8F87" }} axisLine={false} tickLine={false} />
                  <Tooltip formatter={(v: number) => formatMoneda(v)} cursor={{ fill: "rgba(0,0,0,0.03)" }} />
                  <Bar dataKey="total" fill="#E1922E" radius={0} />
                </BarChart>
              </ResponsiveContainer>
            </div>
          )}
        </section>
      </div>
    </div>
  );
}
