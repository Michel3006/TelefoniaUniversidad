import { useState } from "react";
import type { ColumnDef } from "@tanstack/react-table";
import { CrudPage } from "../../components/crud/CrudPage";
import { useEstados, usePlanes, useSims } from "../../lib/queries";
import type { Sim } from "../../lib/types";
import { StatusPill } from "../../components/ui/StatusPill";
import { TextField } from "../../components/ui/Field";

export function SimsPage() {
  const estados = useEstados();
  const planes = usePlanes();
  const [busqueda, setBusqueda] = useState("");

  const nombreEstado = (id: number | null) => estados.data?.find((e) => e.id === id)?.nombre ?? null;
  const nombrePlan = (id: number | null) => planes.data?.find((p) => p.id === id)?.nombre ?? null;

  const useListaFiltrada = useSims;

  const columnas: ColumnDef<Sim, any>[] = [
    { header: "Número", accessorKey: "numero", cell: (c) => <span className="dato">{c.getValue()}</span> },
    { header: "ICCID", accessorKey: "iccid", cell: (c) => <span className="dato">{c.getValue() ?? "—"}</span> },
    { header: "IMSI", accessorKey: "imsi", cell: (c) => <span className="dato">{c.getValue() ?? "—"}</span> },
    { header: "Plan", accessorKey: "plan_id", cell: (c) => <span className="dato">{nombrePlan(c.getValue()) ?? "—"}</span> },
    { header: "Operador", accessorKey: "operador", cell: (c) => <span className="dato">{c.getValue() ?? "ETECSA"}</span> },
    { header: "Estado", accessorKey: "estado_id", cell: (c) => <StatusPill estado={nombreEstado(c.getValue())} /> },
  ];

  return (
    <div className="space-y-4">
      <div className="max-w-xs">
        <TextField
          label="Buscar por número, ICCID o IMSI"
          value={busqueda}
          onChange={(e) => setBusqueda(e.target.value)}
          dato
          placeholder="53…, 8934…"
        />
      </div>
      <CrudPage<Sim>
        titulo="SIMs"
        entidadKey="sims"
        basePath="/sims"
        useLista={() => {
          const q = useListaFiltrada();
          if (!busqueda) return q;
          return {
            ...q,
            data: q.data?.filter(
              (s) =>
                s.numero.toLowerCase().includes(busqueda.toLowerCase()) ||
                s.iccid?.toLowerCase().includes(busqueda.toLowerCase()) ||
                s.imsi?.includes(busqueda)
            ),
          } as typeof q;
        }}
        columnas={columnas}
        nombreItem={(s) => s.numero || s.iccid || `SIM ${s.id}`}
        campos={[
          { name: "numero", label: "Número", type: "telefono", required: true, max: 30 },
          { name: "iccid", label: "ICCID", type: "numero", dato: true, min: 15, max: 20 },
          { name: "imsi", label: "IMSI", type: "numero", dato: true, min: 15, max: 15 },
          { name: "operador", label: "Operador", type: "text", max: 30 },
          {
            name: "plan_id",
            label: "Plan",
            type: "select",
            options: (planes.data ?? []).map((p) => ({ value: p.id, label: p.nombre })),
          },
          {
            name: "estado_id",
            label: "Estado",
            type: "select",
            options: (estados.data ?? []).map((e) => ({ value: e.id, label: e.nombre })),
          },
        ]}
      />
    </div>
  );
}