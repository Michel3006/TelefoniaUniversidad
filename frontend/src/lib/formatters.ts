export function formatFecha(iso: string | null | undefined): string {
  if (!iso) return "—";
  const d = new Date(iso.length === 10 ? `${iso}T00:00:00` : iso);
  if (Number.isNaN(d.getTime())) return iso;
  return d.toLocaleDateString("es-CU", { day: "2-digit", month: "2-digit", year: "numeric" });
}

export function formatFechaHora(iso: string | null | undefined): string {
  if (!iso) return "—";
  const d = new Date(iso);
  if (Number.isNaN(d.getTime())) return iso;
  return `${d.toLocaleDateString("es-CU", { day: "2-digit", month: "2-digit", year: "numeric" })} ${d.toLocaleTimeString(
    "es-CU",
    { hour: "2-digit", minute: "2-digit" }
  )}`;
}

export function formatMoneda(monto: string | number | null | undefined, moneda = "CUP"): string {
  if (monto === null || monto === undefined || monto === "") return "—";
  const n = typeof monto === "string" ? Number(monto) : monto;
  if (Number.isNaN(n)) return String(monto);
  const fmt = n.toLocaleString("es-CU", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  return moneda === "CUP" ? `$ ${fmt}` : `${moneda} ${fmt}`;
}

export function periodoActual(): string {
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}`;
}

export function diasHasta(iso: string | null | undefined): number | null {
  if (!iso) return null;
  const hoy = new Date();
  hoy.setHours(0, 0, 0, 0);
  const fin = new Date(`${iso.slice(0, 10)}T00:00:00`);
  return Math.round((fin.getTime() - hoy.getTime()) / 86_400_000);
}
