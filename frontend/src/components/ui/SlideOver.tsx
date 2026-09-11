import { useEffect } from "react";
import type { ReactNode } from "react";
import { Button } from "./Button";

interface SlideOverProps {
  abierto: boolean;
  titulo: string;
  onCerrar: () => void;
  children: ReactNode;
  footer?: ReactNode;
}

// Panel lateral de 480px desde la derecha. Es el reemplazo del modal
// centrado en todo el sistema: mantiene la tabla visible (atenuada)
// detrás, para no perder el contexto de lo que se estaba mirando.
export function SlideOver({ abierto, titulo, onCerrar, children, footer }: SlideOverProps) {
  useEffect(() => {
    if (!abierto) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") onCerrar();
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [abierto, onCerrar]);

  return (
    <div
      aria-hidden={!abierto}
      className={`fixed inset-0 z-30 ${abierto ? "pointer-events-auto" : "pointer-events-none"}`}
    >
      <div
        onClick={onCerrar}
        className={`absolute inset-0 bg-tinta transition-opacity duration-200 ${
          abierto ? "opacity-30" : "opacity-0"
        }`}
      />
      <aside
        className={`absolute right-0 top-0 h-full w-full max-w-[480px] border-l border-filete bg-papel-alto transition-transform duration-200 ease-out ${
          abierto ? "translate-x-0" : "translate-x-full"
        }`}
      >
        <div className="flex h-full flex-col">
          <header className="flex items-center justify-between border-b border-filete px-5 py-4">
            <h2 className="text-base font-semibold text-tinta">{titulo}</h2>
            <Button variant="texto" onClick={onCerrar}>
              Cerrar
            </Button>
          </header>
          <div className="flex-1 overflow-y-auto px-5 py-5">{children}</div>
          {footer && <footer className="border-t border-filete px-5 py-4">{footer}</footer>}
        </div>
      </aside>
    </div>
  );
}
