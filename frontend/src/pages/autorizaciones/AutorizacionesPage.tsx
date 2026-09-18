import type { ColumnDef } from "@tanstack/react-table";
import { CrudPage } from "../../components/crud/CrudPage";
import { useAutorizaciones, usePersonas, useSims } from "../../lib/queries";
import type { AutorizacionExceso } from "../../lib/types";
import { formatFecha, formatMoneda } from "../../lib/formatters";

export function AutorizacionesPage() {
  const sims = useSims();
  const personas = usePersonas();

  const nombreSim = (id: number) => {
    const s = sims.data?.find((x) => x.id === id);
    return s ? s.numero || s.iccid || `SIM ${s.id}` : `SIM ${id}`;
  };

  const nombrePersona = (id: number) => {
    const p = personas.data?.find((x) => x.id === id);
    return p ? `${p.nombre} ${p.apellido}`.trim() : `Persona ${id}`;
  };

  const columnas: ColumnDef<AutorizacionExceso, any>[] = [
    { header: "SIM", accessorKey: "sim_id", cell: (c) => <span className="dato">{nombreSim(c.getValue())}</span> },
    { header: "Persona", accessorKey: "persona_id", cell: (c) => nombrePersona(c.getValue()) },
    { header: "Límite autorizado (CUP)", accessorKey: "limite_autorizado", cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span> },
    { header: "Desde", accessorKey: "fecha_inicio", cell: (c) => formatFecha(c.getValue()) },
    { header: "Hasta", accessorKey: "fecha_fin", cell: (c) => formatFecha(c.getValue()) },
    { header: "Motivo", accessorKey: "motivo", cell: (c) => c.getValue() ?? "—" },
    { header: "Responsable", accessorKey: "responsable", cell: (c) => c.getValue() ?? "—" },
  ];

  return (
    <CrudPage<AutorizacionExceso>
      titulo="Autorizaciones de exceso"
      entidadKey="autorizaciones"
      basePath="/autorizaciones"
      useLista={useAutorizaciones}
      columnas={columnas}
      nombreItem={(a) => `autorización de la SIM ${nombreSim(a.sim_id)}`}
      descripcionVacio="Todavía no hay autorizaciones de exceso. Sólo el administrador puede crearlas."
      campos={[
        {
          name: "sim_id",
          label: "SIM",
          type: "select",
          required: true,
          options: (sims.data ?? []).map((s) => ({ value: s.id, label: s.numero || s.iccid || `SIM ${s.id}` })),
        },
        {
          name: "persona_id",
          label: "Persona autorizada",
          type: "select",
          required: true,
          options: (personas.data ?? []).map((p) => ({ value: p.id, label: `${p.nombre} ${p.apellido}`.trim() })),
        },
        { name: "limite_autorizado", label: "Límite autorizado (CUP)", type: "decimal", required: true, max: 15 },
        { name: "fecha_inicio", label: "Desde", type: "date", required: true },
        { name: "fecha_fin", label: "Hasta", type: "date" },
        { name: "motivo", label: "Motivo", type: "textarea", max: 500 },
        { name: "responsable", label: "Responsable", type: "text", max: 150 },
        { name: "observaciones", label: "Observaciones", type: "textarea", max: 500 },
      ]}
    />
  );
}