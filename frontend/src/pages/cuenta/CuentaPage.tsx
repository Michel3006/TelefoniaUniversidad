// C1/A2: página de cuenta para la primera sesión. Si el backend bloquea la
// cuenta con `debe_cambiar_password`, ProtectedRoute redirige acá y no se puede
// navegar hasta completar el cambio de contraseña.
import { useState } from "react";
import type { FormEvent } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../lib/auth-context";
import { api, ApiError } from "../../lib/api";
import { Button } from "../../components/ui/Button";
import { TextField } from "../../components/ui/Field";

export function CuentaPage() {
  const { user, recargar } = useAuth();
  const navigate = useNavigate();
  const [passwordActual, setPasswordActual] = useState("");
  const [passwordNueva, setPasswordNueva] = useState("");
  const [confirmacion, setConfirmacion] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [enviando, setEnviando] = useState(false);

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    if (!passwordActual) {
      setError("Ingresá tu contraseña actual.");
      return;
    }
    if (passwordNueva.length < 10) {
      setError("La nueva contraseña debe tener al menos 10 caracteres.");
      return;
    }
    if (!/[A-Za-z]/.test(passwordNueva) || !/\d/.test(passwordNueva)) {
      setError("La nueva contraseña debe contener letras y números.");
      return;
    }
    if (passwordNueva !== confirmacion) {
      setError("Las contraseñas nuevas no coinciden.");
      return;
    }
    setEnviando(true);
    try {
      await api("/auth/cambiar-password", {
        method: "POST",
        json: { password_actual: passwordActual, password_nueva: passwordNueva },
      });
      await recargar();
      navigate("/", { replace: true });
    } catch (err) {
      setError(err instanceof ApiError ? err.detail : "No se pudo cambiar la contraseña.");
    } finally {
      setEnviando(false);
    }
  }

  return (
    <div className="mx-auto max-w-md py-10">
      <h2 className="text-lg font-semibold text-tinta">Cambiar contraseña</h2>
      <p className="mt-1 text-sm text-neutro">
        {user?.debe_cambiar_password
          ? "El sistema requiere que cambies la contraseña antes de continuar."
          : "Actualizá la contraseña de tu cuenta."}
      </p>

      <form onSubmit={onSubmit} className="mt-6 space-y-4 rounded border border-filete bg-papel-alto p-5">
        <TextField
          label="Contraseña actual"
          type="password"
          value={passwordActual}
          onChange={(e) => setPasswordActual(e.target.value)}
          required
          autoFocus
        />
        <TextField
          label="Contraseña nueva"
          type="password"
          value={passwordNueva}
          onChange={(e) => setPasswordNueva(e.target.value)}
          required
          hint="Mínimo 10 caracteres, con letras y números."
        />
        <TextField
          label="Confirmar contraseña nueva"
          type="password"
          value={confirmacion}
          onChange={(e) => setConfirmacion(e.target.value)}
          required
        />
        {error && <p className="text-sm text-linea-baja">{error}</p>}
        <Button type="submit" variant="primario" className="w-full justify-center" disabled={enviando}>
          {enviando ? "Guardando…" : "Guardar"}
        </Button>
      </form>
    </div>
  );
}