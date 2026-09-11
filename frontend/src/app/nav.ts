import type { LucideIcon } from "lucide-react";
import {
  Building2,
  FileText,
  Gauge,
  History,
  Landmark,
  Phone,
  PhoneCall,
  Radio,
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
      { label: "Departamentos", to: "/departamentos", icon: UsersRound },
      { label: "Locales", to: "/locales", icon: Building2 },
    ],
  },
  {
    titulo: "Recursos",
    items: [
      { label: "Líneas", to: "/lineas", icon: PhoneCall },
      { label: "Teléfonos", to: "/telefonos", icon: Phone },
      { label: "Extensiones", to: "/extensiones", icon: Radio },
      { label: "Dispositivos", to: "/dispositivos", icon: Smartphone },
      { label: "SIMs", to: "/sims", icon: Tags },
    ],
  },
  {
    titulo: "Contratos",
    items: [
      { label: "Contratos", to: "/contratos", icon: FileText },
      { label: "Planes", to: "/planes", icon: FileText },
    ],
  },
  {
    titulo: "Catálogos",
    items: [
      { label: "Estados", to: "/estados", icon: Tags },
      { label: "Operadores", to: "/operadores", icon: Landmark },
    ],
  },
  {
    titulo: null,
    items: [
      { label: "Costes", to: "/costes", icon: FileText },
      { label: "Asignaciones", to: "/asignaciones", icon: Shuffle },
      { label: "Historial", to: "/historial", icon: History },
    ],
  },
  {
    titulo: "Administración",
    items: [{ label: "Usuarios", to: "/usuarios", icon: Users, soloAdmin: true }],
  },
];
