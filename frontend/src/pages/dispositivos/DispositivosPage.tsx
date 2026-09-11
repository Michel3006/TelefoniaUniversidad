import type { ColumnDef } from "@tanstack/react-table";
import { CrudPage } from "../../components/crud/CrudPage";
import { useDispositivos, useEstados, useLineas, useLocales } from "../../lib/queries";
import type { Dispositivo } from "../../lib/types";
import { StatusPill } from "../../components/ui/StatusPill";

export function DispositivosPage() {
  const estados = useEstados();
  const lineas = useLineas();
  const locales = useLocales();

  const nombreEstado = (id: number | null) => estados.data?.find((e) => e.id === id)?.nombre ?? null;
  const nombreLinea = (id: number | null) => lineas.data?.find((l) => l.id === id)?.numero ?? "—";
  const nombreLocal = (id: number | null) => {
    const l = locales.data?.find((x) => x.id === id);
    return l ? [l.piso, l.oficina].filter(Boolean).join(" · ") || `Local ${l.id}` : "—";
  };

  const columnas: ColumnDef<Dispositivo, any>[] = [
    { header: "Marca", accessorKey: "marca" },
    { header: "Modelo", accessorKey: "modelo" },
    { header: "IMEI", accessorKey: "imei", cell: (c) => <span className="dato">{c.getValue()}</span> },
    { header: "Línea", accessorKey: "linea_id", cell: (c) => <span className="dato">{nombreLinea(c.getValue())}</span> },
    { header: "Local", accessorKey: "local_id", cell: (c) => nombreLocal(c.getValue()) },
    { header: "Estado", accessorKey: "estado_id", cell: (c) => <StatusPill estado={nombreEstado(c.getValue())} /> },
  ];

  return (
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
          name: "linea_id",
          label: "Línea asignada",
          type: "select",
          options: (lineas.data ?? []).map((l) => ({ value: l.id, label: l.numero })),
        },
        {
          name: "local_id",
          label: "Local",
          type: "select",
          options: (locales.data ?? []).map((l) => ({ value: l.id, label: [l.piso, l.oficina].filter(Boolean).join(" · ") || `Local ${l.id}` })),
        },
        {
          name: "estado_id",
          label: "Estado",
          type: "select",
          options: (estados.data ?? []).map((e) => ({ value: e.id, label: e.nombre })),
        },
      ]}
    />
  );
}
