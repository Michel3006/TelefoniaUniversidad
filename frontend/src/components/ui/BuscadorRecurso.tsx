import { useState } from "react";
import type { UseQueryResult } from "@tanstack/react-query";
import { Search } from "lucide-react";

interface BuscadorRecursoProps<T> {
  placeholder: string;
  useBuscar: (q: string) => UseQueryResult<T[], Error>;
  obtenerId: (item: T) => number;
  obtenerEtiqueta: (item: T) => string;
}

export function BuscadorRecurso<T>({ placeholder, useBuscar, obtenerId, obtenerEtiqueta }: BuscadorRecursoProps<T>) {
  const [q, setQ] = useState("");
  const resultado = useBuscar(q);
  const activa = q.trim().length > 0;
  const items = activa ? (resultado.data ?? []) : [];

  return (
    <div className="relative">
      <div className="relative">
        <Search size={16} className="pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-neutro" />
        <input
          type="search"
          value={q}
          onChange={(e) => setQ(e.target.value)}
          placeholder={placeholder}
          className="w-full border border-filete bg-papel-alto py-2 pl-9 pr-3 text-sm text-tinta placeholder:text-neutro focus:border-tinta focus:outline-none"
        />
      </div>
      {activa && (
        <div className="absolute z-10 mt-1 w-full border border-filete bg-papel shadow-lg">
          {resultado.isLoading && <p className="px-3 py-2 text-sm text-neutro">Buscando…</p>}
          {!resultado.isLoading && items.length === 0 && <p className="px-3 py-2 text-sm text-neutro">Sin coincidencias.</p>}
          {!resultado.isLoading && items.length > 0 && (
            <ul className="divide-y divide-filete">
              {items.slice(0, 6).map((item) => (
                <li key={obtenerId(item)} className="flex items-center gap-2 px-3 py-2 text-sm text-tinta hover:bg-papel-alto">
                  <span className="min-w-0 flex-1 truncate">{obtenerEtiqueta(item)}</span>
                  <span className="dato text-neutro">#{obtenerId(item)}</span>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  );
}