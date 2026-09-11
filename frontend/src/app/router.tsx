import { BrowserRouter, Route, Routes } from "react-router-dom";
import { AppShell } from "../components/layout/AppShell";
import { ProtectedRoute, AdminRoute } from "./ProtectedRoute";

import { LoginPage } from "../pages/login/LoginPage";
import { DashboardPage } from "../pages/dashboard/DashboardPage";
import { PersonasPage } from "../pages/personas/PersonasPage";
import { DepartamentosPage } from "../pages/departamentos/DepartamentosPage";
import { LocalesPage } from "../pages/locales/LocalesPage";
import { LineasPage } from "../pages/lineas/LineasPage";
import { TelefonosPage } from "../pages/telefonos/TelefonosPage";
import { ExtensionesPage } from "../pages/extensiones/ExtensionesPage";
import { DispositivosPage } from "../pages/dispositivos/DispositivosPage";
import { SimsPage } from "../pages/sims/SimsPage";
import { EstadosPage } from "../pages/estados/EstadosPage";
import { OperadoresPage } from "../pages/operadores/OperadoresPage";
import { ContratosPage } from "../pages/contratos/ContratosPage";
import { PlanesPage } from "../pages/planes/PlanesPage";
import { CostesPage } from "../pages/costes/CostesPage";
import { AsignacionesPage } from "../pages/asignaciones/AsignacionesPage";
import { UsuariosPage } from "../pages/usuarios/UsuariosPage";
import { HistorialPage } from "../pages/historial/HistorialPage";

export function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route
          element={
            <ProtectedRoute>
              <AppShell />
            </ProtectedRoute>
          }
        >
          <Route path="/" element={<DashboardPage />} />
          <Route path="/personas" element={<PersonasPage />} />
          <Route path="/departamentos" element={<DepartamentosPage />} />
          <Route path="/locales" element={<LocalesPage />} />
          <Route path="/lineas" element={<LineasPage />} />
          <Route path="/telefonos" element={<TelefonosPage />} />
          <Route path="/extensiones" element={<ExtensionesPage />} />
          <Route path="/dispositivos" element={<DispositivosPage />} />
          <Route path="/sims" element={<SimsPage />} />
          <Route path="/estados" element={<EstadosPage />} />
          <Route path="/operadores" element={<OperadoresPage />} />
          <Route path="/contratos" element={<ContratosPage />} />
          <Route path="/planes" element={<PlanesPage />} />
          <Route path="/costes" element={<CostesPage />} />
          <Route path="/asignaciones" element={<AsignacionesPage />} />
          <Route path="/historial" element={<HistorialPage />} />
          <Route
            path="/usuarios"
            element={
              <AdminRoute>
                <UsuariosPage />
              </AdminRoute>
            }
          />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
