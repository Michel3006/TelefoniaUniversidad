import { Search } from "lucide-react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../lib/auth-context";

export function Topbar() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  return (
    <header className="flex h-14 items-center gap-6 border-b-2 border-senal bg-papel-alto px-5">
      <div className="flex min-w-0 shrink-0 items-center gap-2.5">
        <img src="/cujae-logo.png" alt="CUJAE" className="h-9 w-auto" />
        <div className="hidden leading-tight md:block">
          <p className="text-sm font-bold text-senal">Sistema de Gestión de Telefonía</p>
          <p className="text-[10px] text-neutro">Dirección de Telecomunicaciones y Redes</p>
        </div>
      </div>

      <div className="hidden max-w-sm flex-1 items-center gap-2 px-8 sm:flex">
        <Search size={16} className="text-neutro" />
        <input
          type="search"
          placeholder="Buscar personas…"
          className="w-full bg-transparent text-sm text-tinta placeholder:text-neutro focus:outline-none"
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              const q = (e.target as HTMLInputElement).value.trim();
              if (q) navigate(`/personas?q=${encodeURIComponent(q)}`);
            }
          }}
        />
      </div>

      <div className="ml-auto flex items-center gap-3 text-sm">
        <span className="text-tinta">{user?.username}</span>
        <span className="h-4 w-px bg-filete" aria-hidden />
        <button onClick={logout} className="text-neutro hover:text-tinta hover:underline">
          Salir
        </button>
      </div>
    </header>
  );
}