import { flexRender, getCoreRowModel, useReactTable } from "@tanstack/react-table";
import type { ColumnDef } from "@tanstack/react-table";
import { EmptyState } from "./EmptyState";

interface DataTableProps<T> {
  columns: ColumnDef<T, any>[];
  data: T[];
  onVer?: (item: T) => void;
  onEditar?: (item: T) => void;
  onBorrar?: (item: T) => void;
  vacioTitulo?: string;
  vacioDescripcion?: string;
}

// Tabla de la casa: encabezados en altas y bajas normales, filete fino
// entre filas, sin cebra ni tarjetas. La columna de acciones aparece
// recién al pasar el mouse por la fila.
export function DataTable<T>({
  columns,
  data,
  onVer,
  onEditar,
  onBorrar,
  vacioTitulo = "Todavía no hay datos cargados.",
  vacioDescripcion,
}: DataTableProps<T>) {
  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
  });

  if (data.length === 0) {
    return <EmptyState titulo={vacioTitulo} descripcion={vacioDescripcion} />;
  }

  return (
    <div className="overflow-x-auto">
      <table className="w-full border-collapse text-left">
        <thead className="sticky top-0 bg-papel">
          {table.getHeaderGroups().map((hg) => (
            <tr key={hg.id} className="border-b border-filete">
              {hg.headers.map((header) => (
                <th key={header.id} className="whitespace-nowrap px-3 py-2 text-[13px] font-semibold text-tinta">
                  {flexRender(header.column.columnDef.header, header.getContext())}
                </th>
              ))}
              {(onVer || onEditar || onBorrar) && <th className="px-3 py-2" />}
            </tr>
          ))}
        </thead>
        <tbody>
          {table.getRowModel().rows.map((row) => (
            <tr key={row.id} className="group border-b border-filete hover:bg-black/[0.015]">
              {row.getVisibleCells().map((cell) => (
                <td key={cell.id} className="whitespace-nowrap px-3 py-2.5 text-sm text-tinta">
                  {flexRender(cell.column.columnDef.cell, cell.getContext())}
                </td>
              ))}
              {(onVer || onEditar || onBorrar) && (
                <td className="whitespace-nowrap px-3 py-2.5 text-right text-sm">
                  <span className="invisible flex justify-end gap-3 group-hover:visible">
                    {onVer && (
                      <button
                        onClick={() => onVer(row.original)}
                        className="font-medium text-tinta underline-offset-2 hover:underline"
                      >
                        Ver
                      </button>
                    )}
                    {onEditar && (
                      <button
                        onClick={() => onEditar(row.original)}
                        className="font-medium text-tinta underline-offset-2 hover:underline"
                      >
                        Editar
                      </button>
                    )}
                    {onBorrar && (
                      <button
                        onClick={() => onBorrar(row.original)}
                        className="font-medium text-linea-baja underline-offset-2 hover:underline"
                      >
                        Eliminar
                      </button>
                    )}
                  </span>
                </td>
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
