import type { ReactNode } from "react";
import { Navigate, useLocation } from "react-router-dom";
import { useAuth } from "../lib/auth-context";

export function ProtectedRoute({ children }: { children: ReactNode }) {
  const { user, loading } = useAuth();
  const location = useLocation();
  if (loading) return null;
  if (!user) return <Navigate to="/login" replace />;
  // C1/A2: el backend marca con `debe_cambiar_password` las cuentas creadas/
  // reseteadas con la password inicial; no se puede seguir navegando sin cambiar.
  if (user.debe_cambiar_password && location.pathname !== "/cuenta")
    return <Navigate to="/cuenta" replace />;
  return <>{children}</>;
}

export function AdminRoute({ children }: { children: ReactNode }) {
  const { isAdmin, loading } = useAuth();
  if (loading) return null;
  if (!isAdmin) return <Navigate to="/" replace />;
  return <>{children}</>;
}
