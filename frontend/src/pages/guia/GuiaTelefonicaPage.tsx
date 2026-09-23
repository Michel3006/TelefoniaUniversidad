import { useMemo, useState } from "react";
import type { ColumnDef } from "@tanstack/react-table";
import { DataTable } from "../../components/ui/DataTable";
import { SlideOver } from "../../components/ui/SlideOver";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { TextField } from "../../components/ui/Field";
import { useGuiaTelefonica } from "../../lib/queries";
import type { GuiaTelefonica } from "../../lib/types";

const NOMBRE_TIPO: Record<string, string> = {
  sim: "SIM",
  telefono: "Teléfono",
  dispositivo: "Dispositivo",
  extension: "Extensión",
};

export function GuiaTelefonicaPage() {
  const guia = useGuiaTelefonica();
  const [busqueda, setBusqueda] = useState("");
  const [ver, setVer] = useState<GuiaTelefonica | null>(null);

  const items = useMemo(() => {
    const lista = guia.data ?? [];
    const q = busqueda.trim().toLowerCase();
    if (!q) return lista;
    return lista.filter((p) =>
      `${p.nombre} ${p.apellido} ${p.apellido_2 ?? ""} ${p.id_empleado ?? ""}`
        .toLowerCase()
        .includes(q)
    );
  }, [guia.data, busqueda]);

  const columnas: ColumnDef<GuiaTelefonica, any>[] = [
    {
      header: "Nombre",
      accessorFn: (p) => `${p.apellido} ${p.nombre}${p.apellido_2 ? ` ${p.apellido_2}` : ""}`,
      cell: (c) => <span className="font-medium text-tinta">{c.getValue()}</span>,
    },
    { header: "Cargo", accessorKey: "cargo", cell: (c) => c.getValue() ?? "—" },
    { header: "Departamento", accessorKey: "departamento", cell: (c) => c.getValue() ?? "—" },
    {
      header: "Extensión",
      accessorKey: "exttelef",
      cell: (c) => <span className="dato">{c.getValue() ?? "—"}</span>,
    },
    {
      header: "Teléfono",
      accessorKey: "telefono",
      cell: (c) => <span className="dato">{c.getValue() ?? "—"}</span>,
    },
  ];

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Guía telefónica</h1>
      </div>
      <div className="border border-filete bg-papel-alto px-4 py-3 text-sm text-neutro">
        Directorio de todas las personas con sus datos y los recursos asociados (SIM, teléfono, dispositivo o
        extensión).
      </div>

      <div className="max-w-xs">
        <TextField
          label="Buscar por nombre o nómina"
          value={busqueda}
          onChange={(e) => setBusqueda(e.target.value)}
          dato
          placeholder="Apellido, nombre…"
        />
      </div>

      {guia.isLoading && <EmptyState titulo="Cargando…" />}
      {guia.isError && (
        <ErrorState mensaje={(guia.error as Error)?.message ?? ""} onReintentar={() => guia.refetch()} />
      )}
      {!guia.isLoading && !guia.isError && (
        <DataTable
          columns={columnas}
          data={items}
          onVer={setVer}
          vacioTitulo={busqueda ? "Ningún resultado para esta búsqueda." : "Todavía no hay personas sincronizadas."}
        />
      )}

      <SlideOver
        abierto={ver !== null}
        titulo={ver ? `${ver.apellido} ${ver.nombre}${ver.apellido_2 ? ` ${ver.apellido_2}` : ""}`.trim() : ""}
        onCerrar={() => setVer(null)}
      >
        {ver && (
          <div className="space-y-5">
            <div>
              <p className="text-sm font-medium text-tinta">Datos</p>
              <dl className="mt-2 space-y-1 text-sm">
                <div className="flex justify-between"><dt className="text-neutro">Nómina</dt><dd className="dato">{ver.id_empleado ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Cargo</dt><dd>{ver.cargo ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Área</dt><dd>{ver.area ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Departamento</dt><dd>{ver.departamento ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Cubículo</dt><dd className="dato">{ver.cubiculo ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Extensión</dt><dd className="dato">{ver.exttelef ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Teléfono</dt><dd className="dato">{ver.telefono ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Documento</dt><dd className="dato">{ver.documento ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Email</dt><dd className="dato">{ver.email ?? "—"}</dd></div>
              </dl>
            </div>
            <div>
              <p className="text-sm font-medium text-tinta">Recursos asociados</p>
              {ver.recursos.length === 0 ? (
                <p className="mt-2 text-sm text-neutro">No tiene recursos asociados.</p>
              ) : (
                <ul className="mt-2 divide-y divide-filete border border-filete">
                  {ver.recursos.map((r) => (
                    <li key={`${r.tipo}-${r.recurso_id}`} className="flex items-center justify-between px-3 py-2 text-sm">
                      <span className="dato text-tinta">{r.etiqueta}</span>
                      <span className="capitalize text-neutro">{NOMBRE_TIPO[r.tipo] ?? r.tipo}</span>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </div>
        )}
      </SlideOver>
    </div>
  );
}