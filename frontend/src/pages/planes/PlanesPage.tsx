import type { ColumnDef } from "@tanstack/react-table";
import { CrudPage } from "../../components/crud/CrudPage";
import { useContratos, usePlanes } from "../../lib/queries";
import type { Plan } from "../../lib/types";
import { formatMoneda } from "../../lib/formatters";

export function PlanesPage() {
  const contratos = useContratos();

  const nombreContrato = (id: number | null) => contratos.data?.find((c) => c.id === id)?.numero ?? "—";

  const columnas: ColumnDef<Plan, any>[] = [
    { header: "Nombre", accessorKey: "nombre" },
    { header: "Operador", accessorKey: "operador", cell: (c) => <span className="dato">{c.getValue() ?? "ETECSA"}</span> },
    { header: "Contrato", accessorKey: "contrato_id", cell: (c) => <span className="dato">{nombreContrato(c.getValue())}</span> },
    {
      header: "Coste mensual",
      accessorKey: "coste_mensual",
      cell: (c) => <span className="dato">{formatMoneda(c.getValue())}</span>,
    },
  ];

  return (
    <CrudPage<Plan>
      titulo="Planes"
      entidadKey="planes"
      basePath="/planes"
      useLista={usePlanes}
      columnas={columnas}
      nombreItem={(p) => p.nombre}
      campos={[
        { name: "nombre", label: "Nombre", type: "text", required: true, max: 150 },
        {
          name: "contrato_id",
          label: "Contrato",
          type: "select",
          options: (contratos.data ?? []).map((c) => ({ value: c.id, label: c.numero })),
        },
        { name: "coste_mensual", label: "Coste mensual", type: "decimal", dato: true, placeholder: "0.00" },
        { name: "descripcion", label: "Descripción", type: "textarea", max: 500 },
      ]}
    />
  );
}