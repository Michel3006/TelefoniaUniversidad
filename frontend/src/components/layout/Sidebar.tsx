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
      className={`flex h-full flex-col bg-tinta text-papel transition-[width] duration-150 ${
        colapsado ? "w-16" : "w-60"
      }`}
    >
      <div className="flex h-14 items-center justify-between px-4">
        {!colapsado && <span className="text-sm font-semibold tracking-tight text-white">Troncal</span>}
        <button
          onClick={() => setColapsado((v) => !v)}
          className="text-papel/60 hover:text-white"
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
                <p className="mb-1 px-3 text-[11px] font-medium text-papel/40">{group.titulo}</p>
              )}
              {items.map((item) => (
                <NavLink
                  key={item.to}
                  to={item.to}
                  end={item.to === "/"}
                  className={({ isActive }) =>
                    `relative flex items-center gap-3 rounded px-3 py-2 text-sm ${
                      isActive ? "text-white" : "text-papel/70 hover:text-white"
                    }`
                  }
                >
                  {({ isActive }) => (
                    <>
                      {isActive && (
                        <span className="absolute left-0 top-1 h-[calc(100%-8px)] w-[2px] bg-senal transition-all" />
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
    </nav>
  );
}
