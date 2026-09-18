// Cliente HTTP mínimo contra el backend FastAPI. Sin librerías extra:
// fetch + manejo de 401 + parseo de errores de FastAPI (`detail`).

export class ApiError extends Error {
  status: number;
  detail: string;

  constructor(status: number, detail: string) {
    super(detail);
    this.name = "ApiError";
    this.status = status;
    this.detail = detail;
  }
}

const VITE_API_URL: string = import.meta.env.VITE_API_URL ?? "http://localhost:8000/api/v1";
const BASE_URL: string = VITE_API_URL.endsWith("/api/v1")
  ? VITE_API_URL
  : `${VITE_API_URL.replace(/\/+$/, "")}/api/v1`;

const TOKEN_KEY = "troncal.token";

export const tokenStore = {
  get: (): string | null => localStorage.getItem(TOKEN_KEY),
  set: (t: string): void => localStorage.setItem(TOKEN_KEY, t),
  clear: (): void => localStorage.removeItem(TOKEN_KEY),
};

interface RequestOptions {
  method?: "GET" | "POST" | "PUT" | "DELETE";
  json?: unknown;
  form?: URLSearchParams;
  formData?: FormData;
}

export async function api<T>(path: string, opts: RequestOptions = {}): Promise<T> {
  const headers: Record<string, string> = {};
  const token = tokenStore.get();
  if (token) headers.Authorization = `Bearer ${token}`;

  let body: BodyInit | undefined;
  if (opts.formData) {
    body = opts.formData;
  } else if (opts.form) {
    body = opts.form;
    headers["Content-Type"] = "application/x-www-form-urlencoded";
  } else if (opts.json !== undefined) {
    body = JSON.stringify(opts.json);
    headers["Content-Type"] = "application/json";
  }

  const res = await fetch(`${BASE_URL}${path}`, {
    method: opts.method ?? "GET",
    headers,
    body,
  });

  if (res.status === 401 && !path.startsWith("/auth/login")) {
    tokenStore.clear();
    if (!window.location.pathname.startsWith("/login")) {
      window.location.assign("/login");
    }
    throw new ApiError(401, "La sesión expiró. Iniciá sesión de nuevo.");
  }

  if (!res.ok) {
    let detail = `No se pudo completar la operación (error ${res.status}).`;
    try {
      const data = await res.json();
      if (typeof data?.detail === "string") {
        detail = data.detail;
      } else if (Array.isArray(data?.detail)) {
        // Errores de validación de FastAPI/Pydantic
        detail = data.detail
          .map((e: { loc?: string[]; msg?: string }) => e.msg ?? "Dato inválido")
          .join(" · ");
      }
    } catch {
      /* respuesta sin cuerpo JSON */
    }
    throw new ApiError(res.status, detail);
  }

  if (res.status === 204) return undefined as T;
  return (await res.json()) as T;
}

export function qs(params: Record<string, string | number | undefined | null>): string {
  const sp = new URLSearchParams();
  for (const [k, v] of Object.entries(params)) {
    if (v !== undefined && v !== null && v !== "") sp.set(k, String(v));
  }
  const s = sp.toString();
  return s ? `?${s}` : "";
}
