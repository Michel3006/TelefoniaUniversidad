import type { ColumnDef } from "@tanstack/react-table";
import { CrudPage } from "../../components/crud/CrudPage";
import { BuscadorRecurso } from "../../components/ui/BuscadorRecurso";
import { useBuscarExtensiones, useEstados, useExtensiones, useTelefonos } from "../../lib/queries";
import type { Extension } from "../../lib/types";
import { StatusPill } from "../../components/ui/StatusPill";

export function ExtensionesPage() {
  const estados = useEstados();
  const telefonos = useTelefonos();

  const nombreEstado = (id: number | null) => estados.data?.find((e) => e.id === id)?.nombre ?? null;
  const nombreTelefono = (id: number | null) => telefonos.data?.find((t) => t.id === id)?.numero ?? "—";

  const columnas: ColumnDef<Extension, any>[] = [
    { header: "Número", accessorKey: "numero", cell: (c) => <span className="dato">{c.getValue()}</span> },
    { header: "Teléfono", accessorKey: "telefono_id", cell: (c) => <span className="dato">{nombreTelefono(c.getValue())}</span> },
    { header: "Estado", accessorKey: "estado_id", cell: (c) => <StatusPill estado={nombreEstado(c.getValue())} /> },
  ];

  return (
    <div className="space-y-4">
      <BuscadorRecurso<Extension>
        placeholder="Buscar por número…"
        useBuscar={useBuscarExtensiones}
        obtenerId={(e) => e.id}
        obtenerEtiqueta={(e) => e.numero}
      />
      <CrudPage<Extension>
      titulo="Extensiones"
      entidadKey="extensiones"
      basePath="/extensiones"
      useLista={useExtensiones}
      columnas={columnas}
      nombreItem={(e) => e.numero}
      campos={[
        { name: "numero", label: "Número", type: "numero", required: true, dato: true, min: 1, max: 6 },
        {
          name: "telefono_id",
          label: "Teléfono",
          type: "select",
          options: (telefonos.data ?? []).map((t) => ({ value: t.id, label: t.numero })),
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
