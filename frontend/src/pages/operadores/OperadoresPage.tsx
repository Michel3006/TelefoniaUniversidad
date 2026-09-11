import type { ColumnDef } from "@tanstack/react-table";
import { CrudPage } from "../../components/crud/CrudPage";
import { useOperadores } from "../../lib/queries";
import type { Operador } from "../../lib/types";

const columnas: ColumnDef<Operador, any>[] = [
  { header: "Nombre", accessorKey: "nombre" },
  { header: "Descripción", accessorKey: "descripcion", cell: (c) => c.getValue() ?? "—" },
];

export function OperadoresPage() {
  return (
    <CrudPage<Operador>
      titulo="Operadores"
      entidadKey="operadores"
      basePath="/operadores"
      useLista={useOperadores}
      columnas={columnas}
      nombreItem={(o) => o.nombre}
      campos={[
        { name: "nombre", label: "Nombre", type: "text", required: true, max: 100 },
        { name: "descripcion", label: "Descripción", type: "textarea", max: 500 },
      ]}
    />
  );
}
