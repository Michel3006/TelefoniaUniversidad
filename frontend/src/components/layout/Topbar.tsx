import { Search } from "lucide-react";
import { useNavigate } from "react-router-dom";
import { useLocation } from "react-router-dom";
import { NAV } from "../../app/nav";
import { useAuth } from "../../lib/auth-context";

function tituloActual(pathname: string): string {
  for (const group of NAV) {
    for (const item of group.items) {
      if (item.to === pathname || (item.to !== "/" && pathname.startsWith(item.to))) {
        return item.label;
      }
    }
  }
  return "Panel";
}

export function Topbar() {
  const { user, logout } = useAuth();
  const location = useLocation();
  const navigate = useNavigate();

  return (
    <header className="flex h-14 items-center justify-between border-b border-filete bg-papel px-5">
      <h1 className="text-sm font-semibold text-tinta">{tituloActual(location.pathname)}</h1>

      <div className="hidden max-w-sm flex-1 items-center gap-2 px-8 sm:flex">
        <Search size={16} className="text-neutro" />
        <input
          type="search"
          placeholder="Buscar personas, líneas, dispositivos…"
          className="w-full bg-transparent text-sm text-tinta placeholder:text-neutro focus:outline-none"
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              const q = (e.target as HTMLInputElement).value.trim();
              if (q) navigate(`/personas?q=${encodeURIComponent(q)}`);
            }
          }}
        />
      </div>

      <div className="flex items-center gap-3 text-sm">
        <span className="text-tinta">{user?.username}</span>
        <span className="h-4 w-px bg-filete" aria-hidden />
        <button onClick={logout} className="text-neutro hover:text-tinta hover:underline">
          Salir
        </button>
      </div>
    </header>
  );
}
