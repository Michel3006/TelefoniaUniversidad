import { useMemo, useState } from "react";
import { useSearchParams } from "react-router-dom";
import type { ColumnDef } from "@tanstack/react-table";
import { DataTable } from "../../components/ui/DataTable";
import { SlideOver } from "../../components/ui/SlideOver";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { useAreas, useAsignacionesPorPersona, useCargos, useDepartamentos, usePersonas } from "../../lib/queries";
import type { Persona } from "../../lib/types";
import { formatFecha } from "../../lib/formatters";

export function PersonasPage() {
  const [params] = useSearchParams();
  const filtro = (params.get("q") ?? "").toLowerCase();

  const personas = usePersonas();
  const departamentos = useDepartamentos();
  const cargos = useCargos();
  const areas = useAreas();
  const [verDetalle, setVerDetalle] = useState<Persona | null>(null);

  const asignaciones = useAsignacionesPorPersona(verDetalle?.id ?? null);

  const nombreDepto = (id: number | null) => departamentos.data?.find((d) => d.id === id)?.nombre ?? "—";
  const nombreCargo = (id: number | null) => cargos.data?.find((c) => c.id === id)?.nombre ?? "—";
  const nombreArea = (id: number | null) => areas.data?.find((a) => a.id === id)?.nombre ?? "—";

  const items = useMemo(() => {
    const lista = personas.data ?? [];
    if (!filtro) return lista;
    return lista.filter((p) =>
      `${p.nombre} ${p.apellido} ${p.apellido_2 ?? ""} ${p.id_empleado ?? ""} ${p.documento ?? ""}`.toLowerCase().includes(filtro)
    );
  }, [personas.data, filtro]);

  const columnas: ColumnDef<Persona, any>[] = [
    { header: "Nombre", accessorFn: (p) => `${p.nombre} ${p.apellido}${p.apellido_2 ? ` ${p.apellido_2}` : ""}` },
    { header: "Cargo", accessorKey: "cargo_id", cell: (c) => nombreCargo(c.getValue()) },
    { header: "Departamento", accessorKey: "departamento_id", cell: (c) => nombreDepto(c.getValue()) },
    { header: "Documento", accessorKey: "documento", cell: (c) => <span className="dato">{c.getValue() ?? "—"}</span> },
  ];

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Personas</h1>
      </div>

      <div className="border border-filete bg-papel-alto px-4 py-3 text-sm text-neutro">
        Los datos de personas se sincronizan desde el sistema institucional (ASSETS_RH) y son de solo lectura.
        Cargalos o actualizalos desde Administración → Sincronización RRHH.
      </div>

      {personas.isLoading && <EmptyState titulo="Cargando…" />}
      {personas.isError && (
        <ErrorState mensaje={(personas.error as Error)?.message ?? ""} onReintentar={() => personas.refetch()} />
      )}
      {!personas.isLoading && !personas.isError && (
        <DataTable
          columns={columnas}
          data={items}
          onVer={setVerDetalle}
          vacioTitulo={filtro ? "Ningún resultado para esta búsqueda." : "Todavía no hay personas sincronizadas."}
          vacioDescripcion={filtro ? undefined : "Ejecutá la sincronización de RRHH para cargar el directorio."}
        />
      )}

      <SlideOver abierto={verDetalle !== null} titulo={verDetalle ? `${verDetalle.nombre} ${verDetalle.apellido}${verDetalle.apellido_2 ? ` ${verDetalle.apellido_2}` : ""}` : ""} onCerrar={() => setVerDetalle(null)}>
        {verDetalle && (
          <div className="space-y-5">
            <div>
              <p className="text-sm font-medium text-tinta">Datos institucionales</p>
              <dl className="mt-2 space-y-1 text-sm">
                <div className="flex justify-between"><dt className="text-neutro">Empleado</dt><dd className="dato">{verDetalle.id_empleado ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Expediente</dt><dd className="dato">{verDetalle.id_expediente ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Cargo</dt><dd>{nombreCargo(verDetalle.cargo_id)}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Área</dt><dd>{nombreArea(verDetalle.area_id)}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Departamento</dt><dd>{nombreDepto(verDetalle.departamento_id)}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Documento</dt><dd className="dato">{verDetalle.documento ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">CCosto</dt><dd className="dato">{verDetalle.id_ccosto ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Altas</dt><dd className="dato">{verDetalle.exttelef ?? "—"}</dd></div>
                <div className="flex justify-between"><dt className="text-neutro">Estado</dt><dd>{verDetalle.baja ? <span className="text-linea-baja">Baja</span> : <span className="text-linea-ok">Activo</span>}</dd></div>
              </dl>
            </div>
            <div>
              <p className="text-sm font-medium text-tinta">Recursos asignados</p>
              {asignaciones.isLoading && <p className="mt-2 text-sm text-neutro">Cargando…</p>}
              {!asignaciones.isLoading && (asignaciones.data ?? []).length === 0 && (
                <p className="mt-2 text-sm text-neutro">No tiene recursos asignados.</p>
              )}
              {(asignaciones.data ?? []).length > 0 && (
                <ul className="mt-2 divide-y divide-filete border border-filete">
                  {asignaciones.data!.map((a) => (
                    <li key={a.id} className="flex items-center justify-between px-3 py-2 text-sm">
                      <div>
                        <p className="capitalize text-tinta">{a.tipo_recurso}</p>
                        <p className="dato text-neutro">desde {formatFecha(a.fecha_inicio)}</p>
                      </div>
                      <span className={a.fecha_fin ? "text-neutro" : "text-linea-ok"}>
                        {a.fecha_fin ? "Finalizada" : "Activa"}
                      </span>
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