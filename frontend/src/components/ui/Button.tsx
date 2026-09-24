import type { ButtonHTMLAttributes } from "react";

type Variant = "primario" | "secundario" | "destructivo" | "texto";

interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: Variant;
}

const base = "inline-flex items-center gap-2 rounded px-3.5 py-2 text-sm font-medium transition-colors disabled:opacity-50 disabled:pointer-events-none";

const variants: Record<Variant, string> = {
  primario: "bg-senal text-white hover:bg-senal/90",
  secundario: "bg-transparent border border-filete text-tinta hover:bg-black/[0.03]",
  destructivo: "bg-transparent text-linea-baja hover:bg-linea-baja/10",
  texto: "bg-transparent text-tinta underline-offset-2 hover:underline px-1 py-0.5",
};

export function Button({ variant = "secundario", className = "", ...props }: ButtonProps) {
  return <button className={`${base} ${variants[variant]} ${className}`} {...props} />;
}
