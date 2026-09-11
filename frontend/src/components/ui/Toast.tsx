import { createContext, useCallback, useContext, useState } from "react";
import type { ReactNode } from "react";

interface ToastItem {
  id: number;
  mensaje: string;
  tipo: "ok" | "error";
}

interface ToastContextValue {
  mostrar: (mensaje: string, tipo?: "ok" | "error") => void;
}

const ToastContext = createContext<ToastContextValue | null>(null);

let nextId = 1;

export function ToastProvider({ children }: { children: ReactNode }) {
  const [items, setItems] = useState<ToastItem[]>([]);

  const mostrar = useCallback((mensaje: string, tipo: "ok" | "error" = "ok") => {
    const id = nextId++;
    setItems((prev) => [...prev, { id, mensaje, tipo }]);
    setTimeout(() => {
      setItems((prev) => prev.filter((i) => i.id !== id));
    }, 4000);
  }, []);

  return (
    <ToastContext.Provider value={{ mostrar }}>
      {children}
      <div className="fixed bottom-4 right-4 z-50 flex flex-col gap-2">
        {items.map((item) => (
          <div
            key={item.id}
            className={`min-w-[240px] max-w-sm border-l-4 bg-papel-alto px-4 py-3 text-sm shadow-none ${
              item.tipo === "error" ? "border-linea-baja text-linea-baja" : "border-linea-ok text-tinta"
            }`}
            role="status"
          >
            {item.mensaje}
          </div>
        ))}
      </div>
    </ToastContext.Provider>
  );
}

export function useToast(): ToastContextValue {
  const ctx = useContext(ToastContext);
  if (!ctx) throw new Error("useToast debe usarse dentro de <ToastProvider>");
  return ctx;
}
