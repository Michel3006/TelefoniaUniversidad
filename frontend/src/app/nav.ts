import type { LucideIcon } from "lucide-react";
import {
  BarChart3,
  BookOpen,
  Building2,
  ClipboardList,
  Database,
  FileText,
  Gauge,
  History,
  Phone,
  Radio,
  ReceiptText,
  ShieldCheck,
  Shuffle,
  Smartphone,
  Tags,
  Users,
  UsersRound,
} from "lucide-react";

export interface NavItem {
  label: string;
  to: string;
  icon: LucideIcon;
  soloAdmin?: boolean;
}

export interface NavGroup {
  titulo: string | null;
  items: NavItem[];
}

export const NAV: NavGroup[] = [
  {
    titulo: null,
    items: [{ label: "Panel", to: "/", icon: Gauge }],
  },
  {
    titulo: "Directorio",
    items: [
      { label: "Personas", to: "/personas", icon: Users },
      { label: "Guía telefónica", to: "/guia-telefonica", icon: BookOpen },
      { label: "Departamentos", to: "/departamentos", icon: UsersRound },
    ],
  },
  {
    titulo: "Recursos",
    items: [
      { label: "Teléfonos", to: "/telefonos", icon: Phone },
      { label: "Extensiones", to: "/extensiones", icon: Radio },
      { label: "Dispositivos", to: "/dispositivos", icon: Smartphone },
      { label: "SIMs", to: "/sims", icon: Tags },
    ],
  },
  {
    titulo: "Contratos",
    items: [{ label: "Contratos", to: "/contratos", icon: FileText }],
  },
  {
    titulo: "Operación",
    items: [
      { label: "Consumo", to: "/consumo", icon: ReceiptText },
      { label: "Reportes", to: "/reportes", icon: BarChart3 },
      { label: "Autorizaciones", to: "/autorizaciones", icon: ShieldCheck, soloAdmin: true },
    ],
  },
  {
    titulo: "Catálogos",
    items: [
      { label: "Estados", to: "/estados", icon: Tags },
      { label: "Cargos", to: "/cargos", icon: UsersRound },
      { label: "Áreas", to: "/areas", icon: Building2 },
    ],
  },
  {
    titulo: null,
    items: [
      { label: "Asignaciones", to: "/asignaciones", icon: Shuffle },
      { label: "Historial", to: "/historial", icon: History, soloAdmin: true },
    ],
  },
  {
    titulo: "Administración",
    items: [
      { label: "Usuarios", to: "/usuarios", icon: Users, soloAdmin: true },
      { label: "Auditoría", to: "/auditoria", icon: ClipboardList, soloAdmin: true },
      { label: "Sincronización RRHH", to: "/sincronizacion", icon: Database, soloAdmin: true },
    ],
  },
];
