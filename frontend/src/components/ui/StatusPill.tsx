// El estado siempre se muestra con color + texto juntos, nunca solo color
// (ver especificación de diseño, sección 4). Los nombres de estado son
// dinámicos (vienen de la tabla `estados` del backend) — se mapean por
// nombre a un color conocido, y a `neutro` si no matchea ninguno.

const MAPA_COLOR: Record<string, string> = {
  activo: "bg-linea-ok",
  activa: "bg-linea-ok",
  baja: "bg-linea-baja",
  inactivo: "bg-linea-baja",
  inactiva: "bg-linea-baja",
  pendiente: "bg-senal",
  "en reparación": "bg-senal",
  "en reparacion": "bg-senal",
};

export function StatusPill({ estado }: { estado: string | null | undefined }) {
  const texto = estado?.trim() || "Sin estado";
  const color = estado ? MAPA_COLOR[estado.trim().toLowerCase()] ?? "bg-neutro" : "bg-neutro";
  return (
    <span className="inline-flex items-center gap-1.5 text-sm text-tinta">
      <span className={`h-2 w-2 shrink-0 rounded-full ${color}`} aria-hidden />
      {texto}
    </span>
  );
}
