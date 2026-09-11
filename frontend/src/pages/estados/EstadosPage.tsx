import type { ColumnDef } from "@tanstack/react-table";
import { CrudPage } from "../../components/crud/CrudPage";
import { useEstados } from "../../lib/queries";
import type { Estado } from "../../lib/types";

const columnas: ColumnDef<Estado, any>[] = [
  { header: "Nombre", accessorKey: "nombre" },
  { header: "Descripción", accessorKey: "descripcion", cell: (c) => c.getValue() ?? "—" },
];

export function EstadosPage() {
  return (
    <CrudPage<Estado>
      titulo="Estados"
      descripcionVacio="Los estados son la base de los indicadores de color en todo el sistema (activo, baja, pendiente...)."
      entidadKey="estados"
      basePath="/estados"
      useLista={useEstados}
      columnas={columnas}
      nombreItem={(e) => e.nombre}
      campos={[
        { name: "nombre", label: "Nombre", type: "text", required: true, max: 50 },
        { name: "descripcion", label: "Descripción", type: "textarea", max: 500 },
      ]}
    />
  );
}
