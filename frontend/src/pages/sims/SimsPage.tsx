import { useState } from "react";
import type { ColumnDef } from "@tanstack/react-table";
import { CrudPage } from "../../components/crud/CrudPage";
import { useEstados, useOperadores, useSims } from "../../lib/queries";
import type { Sim } from "../../lib/types";
import { StatusPill } from "../../components/ui/StatusPill";
import { TextField } from "../../components/ui/Field";

export function SimsPage() {
  const operadores = useOperadores();
  const estados = useEstados();
  const [busqueda, setBusqueda] = useState("");

  const nombreOperador = (id: number | null) => operadores.data?.find((o) => o.id === id)?.nombre ?? "—";
  const nombreEstado = (id: number | null) => estados.data?.find((e) => e.id === id)?.nombre ?? null;

  const columnas: ColumnDef<Sim, any>[] = [
    { header: "ICCID", accessorKey: "iccid", cell: (c) => <span className="dato">{c.getValue()}</span> },
    { header: "IMSI", accessorKey: "imsi", cell: (c) => <span className="dato">{c.getValue() ?? "—"}</span> },
    { header: "Operador", accessorKey: "operador_id", cell: (c) => nombreOperador(c.getValue()) },
    { header: "Estado", accessorKey: "estado_id", cell: (c) => <StatusPill estado={nombreEstado(c.getValue())} /> },
  ];

  const useListaFiltrada = useSims;

  return (
    <div className="space-y-4">
      <div className="max-w-xs">
        <TextField
          label="Buscar por ICCID o IMSI"
          value={busqueda}
          onChange={(e) => setBusqueda(e.target.value)}
          dato
          placeholder="8934…"
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
              (s) => s.iccid.toLowerCase().includes(busqueda.toLowerCase()) || (s.imsi ?? "").includes(busqueda)
            ),
          } as typeof q;
        }}
        columnas={columnas}
        nombreItem={(s) => s.iccid}
        campos={[
          { name: "iccid", label: "ICCID", type: "numero", required: true, dato: true, min: 15, max: 20 },
          { name: "imsi", label: "IMSI", type: "numero", dato: true, min: 15, max: 15 },
          {
            name: "operador_id",
            label: "Operador",
            type: "select",
            options: (operadores.data ?? []).map((o) => ({ value: o.id, label: o.nombre })),
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
