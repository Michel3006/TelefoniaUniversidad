import { useState } from "react";
import { NavLink } from "react-router-dom";
import { ChevronsLeft, ChevronsRight } from "lucide-react";
import { NAV } from "../../app/nav";
import { useAuth } from "../../lib/auth-context";

export function Sidebar() {
  const [colapsado, setColapsado] = useState(false);
  const { isAdmin } = useAuth();

  return (
    <nav
      className={`flex h-full flex-col border-r border-filete bg-papel-alto transition-[width] duration-150 ${
        colapsado ? "w-16" : "w-60"
      }`}
    >
      <div className="flex h-14 items-center justify-between gap-2 border-b border-filete px-3">
        {!colapsado && (
          <div className="flex min-w-0 items-center gap-2">
            <img src="/cujae-logo.png" alt="CUJAE" className="h-8 w-auto shrink-0" />
            <div className="min-w-0 leading-tight">
              <p className="truncate text-sm font-bold text-senal">Sistema de Telefonía</p>
              <p className="truncate text-[10px] text-neutro">CUJAE · Telecomunicaciones</p>
            </div>
          </div>
        )}
        <button
          onClick={() => setColapsado((v) => !v)}
          className="text-neutro hover:text-senal"
          aria-label={colapsado ? "Expandir navegación" : "Colapsar navegación"}
        >
          {colapsado ? <ChevronsRight size={18} /> : <ChevronsLeft size={18} />}
        </button>
      </div>

      <div className="flex-1 overflow-y-auto px-2 pb-4">
        {NAV.map((group, i) => {
          const items = group.items.filter((it) => !it.soloAdmin || isAdmin);
          if (items.length === 0) return null;
          return (
            <div key={i} className="mt-4 first:mt-1">
              {group.titulo && !colapsado && (
                <p className="mb-1 px-3 text-[11px] font-bold uppercase tracking-widest text-neutro">
                  {group.titulo}
                </p>
              )}
              {items.map((item) => (
                <NavLink
                  key={item.to}
                  to={item.to}
                  end={item.to === "/"}
                  className={({ isActive }) =>
                    `relative flex items-center gap-3 rounded px-3 py-2 text-sm ${
                      isActive
                        ? "bg-verde-suave font-semibold text-senal"
                        : "text-[#4c514c] hover:bg-verde-suave hover:text-senal"
                    }`
                  }
                >
                  {({ isActive }) => (
                    <>
                      {isActive && (
                        <span className="absolute left-0 top-1 h-[calc(100%-8px)] w-[3px] bg-senal" />
                      )}
                      <item.icon size={17} className="shrink-0" />
                      {!colapsado && <span>{item.label}</span>}
                    </>
                  )}
                </NavLink>
              ))}
            </div>
          );
        })}
      </div>

      <div className="flex items-center gap-2.5 border-t border-filete px-3 py-3">
        <img src="/cujae-logo.png" alt="CUJAE" className="h-9 w-auto shrink-0 opacity-95" />
        {!colapsado && (
          <p className="text-[10.5px] italic leading-snug text-neutro">
            Universidad Tecnológica de La Habana «José Antonio Echeverría»
            <br />
            «Cada uno cuenta.»
          </p>
        )}
      </div>
    </nav>
  );
}