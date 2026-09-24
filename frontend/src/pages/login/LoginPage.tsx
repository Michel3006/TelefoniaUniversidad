import { useState } from "react";
import type { FormEvent } from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "../../lib/auth-context";
import { ApiError } from "../../lib/api";
import { Button } from "../../components/ui/Button";
import { TextField } from "../../components/ui/Field";

export function LoginPage() {
  const { user, login, loading } = useAuth();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [enviando, setEnviando] = useState(false);

  if (!loading && user) return <Navigate to="/" replace />;

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    if (!username.trim() || !password) {
      setError("Ingresá usuario y contraseña.");
      return;
    }
    setEnviando(true);
    try {
      await login(username, password);
    } catch (err) {
      setError(err instanceof ApiError ? err.detail : "No se pudo iniciar sesión.");
    } finally {
      setEnviando(false);
    }
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-papel px-4">
      <div className="w-full max-w-sm border border-filete border-t-4 border-t-senal bg-papel-alto p-8 text-center shadow-lg">
        <img src="/cujae-logo.png" alt="Escudo de la CUJAE" className="mx-auto mb-3 h-24 w-auto" />
        <p className="text-lg font-bold tracking-tight text-senal">Sistema de Gestión de Telefonía</p>
        <p className="mt-1 text-sm text-neutro">Inventario, costos y consumo de servicios telefónicos</p>

        <form onSubmit={onSubmit} className="mt-6 space-y-4 text-left">
          <TextField
            label="Usuario"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            autoFocus
            required
          />
          <TextField
            label="Contraseña"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          {error && <p className="text-sm text-linea-baja">{error}</p>}
          <Button type="submit" variant="primario" className="w-full justify-center" disabled={enviando}>
            {enviando ? "Ingresando…" : "Ingresar"}
          </Button>
        </form>

        <p className="mt-6 border-t border-filete pt-4 text-[11px] leading-relaxed text-neutro">
          Universidad Tecnológica de La Habana
          <br />
          «José Antonio Echeverría» · CUJAE
          <br />
          Calle 114 entre Ciclovía y Rotonda, Marianao
        </p>
        <p className="mt-3 text-[11px] italic text-neutro">
          Dirección de Telecomunicaciones y Redes · «Cada uno cuenta.»
        </p>
      </div>
    </div>
  );
}