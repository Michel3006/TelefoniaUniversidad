import type { ColumnDef } from "@tanstack/react-table";
import { CrudPage } from "../../components/crud/CrudPage";
import { BuscadorRecurso } from "../../components/ui/BuscadorRecurso";
import { useBuscarDispositivos, useDispositivos, useEstados, useSims } from "../../lib/queries";
import type { Dispositivo } from "../../lib/types";
import { StatusPill } from "../../components/ui/StatusPill";

export function DispositivosPage() {
  const estados = useEstados();
  const sims = useSims();

  const nombreEstado = (id: number | null) => estados.data?.find((e) => e.id === id)?.nombre ?? null;
  const nombreSim = (id: number | null) => {
    const s = sims.data?.find((x) => x.id === id);
    return s ? s.numero || s.iccid || `SIM ${s.id}` : "—";
  };

  const columnas: ColumnDef<Dispositivo, any>[] = [
    { header: "Marca", accessorKey: "marca" },
    { header: "Modelo", accessorKey: "modelo" },
    { header: "IMEI", accessorKey: "imei", cell: (c) => <span className="dato">{c.getValue()}</span> },
    { header: "SIM", accessorKey: "sim_id", cell: (c) => <span className="dato">{nombreSim(c.getValue())}</span> },
    { header: "Estado", accessorKey: "estado_id", cell: (c) => <StatusPill estado={nombreEstado(c.getValue())} /> },
    { header: "Observaciones", accessorKey: "observaciones", cell: (c) => c.getValue() ?? "—" },
  ];

  return (
    <div className="space-y-4">
      <BuscadorRecurso<Dispositivo>
        placeholder="Buscar por IMEI, marca o modelo…"
        useBuscar={useBuscarDispositivos}
        obtenerId={(d) => d.id}
        obtenerEtiqueta={(d) => `${d.marca} ${d.modelo} · ${d.imei}`}
      />
      <CrudPage<Dispositivo>
      titulo="Dispositivos"
      entidadKey="dispositivos"
      basePath="/dispositivos"
      useLista={useDispositivos}
      columnas={columnas}
      nombreItem={(d) => `${d.marca} ${d.modelo}`}
      campos={[
        { name: "marca", label: "Marca", type: "text", required: true, max: 100 },
        { name: "modelo", label: "Modelo", type: "text", required: true, max: 100 },
        { name: "imei", label: "IMEI", type: "numero", required: true, dato: true, min: 15, max: 15 },
        {
          name: "sim_id",
          label: "SIM asignada",
          type: "select",
          options: (sims.data ?? []).map((l) => ({ value: l.id, label: l.numero || l.iccid || `SIM ${l.id}` })),
        },
        {
          name: "estado_id",
          label: "Estado",
          type: "select",
          options: (estados.data ?? []).map((e) => ({ value: e.id, label: e.nombre })),
        },
        { name: "observaciones", label: "Observaciones", type: "textarea", max: 500 },
      ]}
      />
    </div>
  );
}
