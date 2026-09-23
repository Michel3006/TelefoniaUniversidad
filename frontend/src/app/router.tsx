import { BrowserRouter, Route, Routes } from "react-router-dom";
import { AppShell } from "../components/layout/AppShell";
import { ProtectedRoute, AdminRoute } from "./ProtectedRoute";

import { LoginPage } from "../pages/login/LoginPage";
import { DashboardPage } from "../pages/dashboard/DashboardPage";
import { ConsumoPage } from "../pages/consumo/ConsumoPage";
import { ReportesPage } from "../pages/reportes/ReportesPage";
import { AutorizacionesPage } from "../pages/autorizaciones/AutorizacionesPage";
import { PersonasPage } from "../pages/personas/PersonasPage";
import { GuiaTelefonicaPage } from "../pages/guia/GuiaTelefonicaPage";
import { DepartamentosPage } from "../pages/departamentos/DepartamentosPage";
import { CargosPage } from "../pages/cargos/CargosPage";
import { AreasPage } from "../pages/areas/AreasPage";
import { TelefonosPage } from "../pages/telefonos/TelefonosPage";
import { ExtensionesPage } from "../pages/extensiones/ExtensionesPage";
import { DispositivosPage } from "../pages/dispositivos/DispositivosPage";
import { SimsPage } from "../pages/sims/SimsPage";
import { EstadosPage } from "../pages/estados/EstadosPage";
import { ContratosPage } from "../pages/contratos/ContratosPage";
import { AsignacionesPage } from "../pages/asignaciones/AsignacionesPage";
import { UsuariosPage } from "../pages/usuarios/UsuariosPage";
import { HistorialPage } from "../pages/historial/HistorialPage";
import { SincronizacionPage } from "../pages/sincronizacion/SincronizacionPage";
import { CuentaPage } from "../pages/cuenta/CuentaPage";

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
          <Route path="/consumo" element={<ConsumoPage />} />
          <Route path="/reportes" element={<ReportesPage />} />
          <Route
            path="/autorizaciones"
            element={
              <AdminRoute>
                <AutorizacionesPage />
              </AdminRoute>
            }
          />
          <Route path="/personas" element={<PersonasPage />} />
          <Route path="/guia-telefonica" element={<GuiaTelefonicaPage />} />
          <Route path="/departamentos" element={<DepartamentosPage />} />
          <Route path="/cargos" element={<CargosPage />} />
          <Route path="/areas" element={<AreasPage />} />
          <Route path="/telefonos" element={<TelefonosPage />} />
          <Route path="/extensiones" element={<ExtensionesPage />} />
          <Route path="/dispositivos" element={<DispositivosPage />} />
          <Route path="/sims" element={<SimsPage />} />
          <Route path="/estados" element={<EstadosPage />} />
          <Route path="/contratos" element={<ContratosPage />} />
          <Route path="/asignaciones" element={<AsignacionesPage />} />
          <Route
            path="/historial"
            element={
              <AdminRoute>
                <HistorialPage />
              </AdminRoute>
            }
          />
          <Route path="/cuenta" element={<CuentaPage />} />
          <Route
            path="/sincronizacion"
            element={
              <AdminRoute>
                <SincronizacionPage />
              </AdminRoute>
            }
          />
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
