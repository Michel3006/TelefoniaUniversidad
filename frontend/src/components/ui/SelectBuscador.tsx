import { useEffect, useMemo, useState } from "react";
import type { UseQueryResult } from "@tanstack/react-query";
import { Search, X } from "lucide-react";
import { FieldWrapper } from "./Field";

export interface ResultadoBusqueda {
  id: number;
  label: string;
}

interface SelectBuscadorProps {
  label: string;
  value: string | number | null;
  onChange: (valor: string) => void;
  error?: string;
  hint?: string;
  required?: boolean;
  placeholder?: string;
  /** Catálogo completo para etiquetar el valor actual y filtrar en local. */
  options?: { value: string | number; label: string }[];
  /** Búsqueda remota opcional (p. ej. personas por nombre). */
  useBuscar?: (q: string) => UseQueryResult<ResultadoBusqueda[], Error>;
  /** Cuántos resultados mostrar cuando no se escribió nada. */
  umbral?: number;
}

const UMBRAL_DEFECTO = 20;

const inputBase =
  "w-full rounded border border-filete bg-papel-alto px-3 py-2 text-sm text-tinta placeholder:text-neutro focus:border-senal";

export function SelectBuscador({
  label,
  value,
  onChange,
  error,
  hint,
  required,
  placeholder = "Escribí para buscar…",
  options = [],
  useBuscar,
  umbral = UMBRAL_DEFECTO,
}: SelectBuscadorProps) {
  const [abierto, setAbierto] = useState(false);
  const [texto, setTexto] = useState("");

  const etiquetaValor = useMemo(() => {
    if (value === null || value === undefined || value === "") return "";
    const op = options.find((o) => String(o.value) === String(value));
    return op?.label ?? `#${value}`;
  }, [options, value]);

  useEffect(() => {
    if (!abierto) setTexto(etiquetaValor);
  }, [etiquetaValor, abierto]);

  const q = texto.trim();
  const remoto = useBuscar ? useBuscar(q) : undefined;
  const remotoData = q && remoto?.data
    ? remoto.data.map((o) => ({ value: o.id, label: o.label }))
    : [];
  const remotoCargando = q ? (remoto?.isLoading ?? false) : false;

  const locales = useMemo(() => {
    const t = q.toLowerCase();
    if (!t) return options.slice(0, umbral);
    return options.filter((o) => o.label.toLowerCase().includes(t)).slice(0, umbral);
  }, [q, options, umbral]);

  const items = q && useBuscar ? remotoData : locales;

  function seleccionar(o: { value: string | number; label: string }) {
    onChange(String(o.value));
    setTexto(o.label);
    setAbierto(false);
  }

  return (
    <FieldWrapper label={label} error={error} hint={hint}>
      <div className="relative">
        <div className="relative">
          <Search size={16} className="pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-neutro" />
          <input
            type="search"
            value={abierto ? texto : etiquetaValor}
            onChange={(e) => {
              setTexto(e.target.value);
              setAbierto(true);
              onChange("");
            }}
            onFocus={() => {
              setAbierto(true);
              setTexto("");
            }}
            onBlur={() => setTimeout(() => setAbierto(false), 120)}
            placeholder={placeholder}
            className={`${inputBase} pl-9 pr-8`}
          />
          {value !== null && value !== undefined && value !== "" && !abierto && (
            <button
              type="button"
              tabIndex={-1}
              onMouseDown={(e) => {
                e.preventDefault();
                onChange("");
                setTexto("");
              }}
              className="absolute right-3 top-1/2 -translate-y-1/2 text-neutro hover:text-tinta"
            >
              <X size={14} />
            </button>
          )}
        </div>

        {abierto && (
          <div className="absolute z-20 mt-1 max-h-64 w-full overflow-y-auto border border-filete bg-papel shadow-lg">
            {remotoCargando && <p className="px-3 py-2 text-sm text-neutro">Buscando…</p>}
            {!q && options.length > umbral && <p className="px-3 py-2 text-sm text-neutro">Escribí para buscar…</p>}
            {!q && options.length > 0 && options.length <= umbral && (
              <p className="px-3 py-2 text-xs text-neutro">{options.length} opciones disponibles</p>
            )}
            {items.length === 0 && !remotoCargando && (
              <p className="px-3 py-2 text-sm text-neutro">Sin resultados.</p>
            )}
            {items.length > 0 && (
              <ul className="divide-y divide-filete">
                {items.map((o) => (
                  <li
                    key={o.value}
                    onMouseDown={(e) => {
                      e.preventDefault();
                      seleccionar(o);
                    }}
                    className="cursor-pointer px-3 py-2 text-sm text-tinta hover:bg-papel-alto"
                  >
                    {o.label}
                  </li>
                ))}
              </ul>
            )}
          </div>
        )}
      </div>
    </FieldWrapper>
  );
}