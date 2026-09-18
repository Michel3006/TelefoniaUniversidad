import type { ColumnDef } from "@tanstack/react-table";
import { CrudPage } from "../../components/crud/CrudPage";
import { useLimites, useSims } from "../../lib/queries";
import type { LimiteConsumo } from "../../lib/types";
import { formatFecha, formatMoneda } from "../../lib/formatters";

export function LimitesPage() {
  const sims = useSims();

  const nombreSim = (id: number) => {
    const s = sims.data?.find((x) => x.id === id);
    return s ? s.numero || s.iccid || `SIM ${s.id}` : `SIM ${id}`;
  };

  const columnas: ColumnDef<LimiteConsumo, any>[] = [
    { header: "SIM", accessorKey: "sim_id", cell: (c) => <span className="dato">{nombreSim(c.getValue())}</span> },
    { header: "Límite (CUP)", accessorKey: "valor_limite", cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span> },
    { header: "Vigente desde", accessorKey: "vigente_desde", cell: (c) => formatFecha(c.getValue()) },
    { header: "Vigente hasta", accessorKey: "vigente_hasta", cell: (c) => formatFecha(c.getValue()) },
    { header: "Observaciones", accessorKey: "observaciones", cell: (c) => c.getValue() ?? "—" },
  ];

  return (
    <CrudPage<LimiteConsumo>
      titulo="Límites de consumo"
      entidadKey="limites"
      basePath="/limites"
      useLista={useLimites}
      columnas={columnas}
      nombreItem={(l) => `límite de la SIM ${nombreSim(l.sim_id)}`}
      descripcionVacio="Todavía no hay límites de consumo cargados. Al importar una factura, las SIMs sin límite no se evalúan contra ninguno."
      campos={[
        {
          name: "sim_id",
          label: "SIM",
          type: "select",
          required: true,
          options: (sims.data ?? []).map((s) => ({ value: s.id, label: s.numero || s.iccid || `SIM ${s.id}` })),
        },
        { name: "valor_limite", label: "Límite (CUP)", type: "decimal", required: true, max: 15 },
        { name: "vigente_desde", label: "Vigente desde", type: "date", required: true },
        { name: "vigente_hasta", label: "Vigente hasta", type: "date" },
        { name: "observaciones", label: "Observaciones", type: "textarea", max: 500 },
      ]}
    />
  );
}