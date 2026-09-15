// Validación de formularios. Centraliza los tipos de campo y las reglas para
// que ningún formulario acepte datos inválidos (letras en campos numéricos,
// emails mal formados, fechas/imposibles, CUIT inválido, etc.).

export type TipoCampo =
  | "text"
  | "textarea"
  | "select" // solo validación de obligatorio; los valores vienen de options
  | "password"
  | "numero" // solo dígitos (IMEI, ICCID, documento, IMSI...)
  | "telefono" // dígitos + espacios + guiones + "+"
  | "decimal" // número con coma o punto decimal
  | "email"
  | "date" // AAAA-MM-DD
  | "periodo" // AAAA-MM
  | "cuit"; // 11 dígitos con dígito verificador

export interface ReglaCampo {
  name: string;
  label: string;
  tipo: TipoCampo;
  required?: boolean;
  min?: number;
  max?: number;
}

export interface FormError {
  [name: string]: string;
}

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

// Limpia el texto al escribir: evita que se ingresen caracteres inválidos.
export function limpiar(tipo: TipoCampo, raw: string): string {
  switch (tipo) {
    case "numero":
    case "cuit":
      return raw.replace(/\D/g, "");
    case "telefono":
      return raw.replace(/[^\d+\- ]/g, "");
    case "decimal": {
      let s = raw.replace(/[^\d.,]/g, "").replace(/,/g, ".");
      const i = s.indexOf(".");
      if (i !== -1) s = s.slice(0, i + 1) + s.slice(i + 1).replace(/\./g, "");
      if (s === ".") s = "";
      return s;
    }
    case "periodo":
      return raw.replace(/[^\d-]/g, "");
    case "email":
      return raw.replace(/\s/g, "");
    default:
      return raw;
  }
}

function verificarCuit(cuit: string): boolean {
  const pesos = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2];
  let suma = 0;
  for (let i = 0; i < 10; i++) suma += Number(cuit[i]) * pesos[i];
  const resto = suma % 11;
  const digito = resto === 0 ? 0 : resto === 1 ? 23 : 11 - resto;
  return Number(cuit[10]) === digito;
}

export function validarCampo(valor: string, campo: ReglaCampo): string | null {
  const v = (valor ?? "").trim();
  const obligatorio = campo.required === true;

  if (obligatorio && v === "") return "Este campo es obligatorio.";
  if (v === "") return null;

  switch (campo.tipo) {
    case "numero": {
      if (!/^\d+$/.test(v)) return "Solo se permiten números.";
      if (campo.max !== undefined && v.length > campo.max)
        return `Debe tener como máximo ${campo.max} dígitos.`;
      if (campo.min !== undefined && v.length < campo.min)
        return `Debe tener al menos ${campo.min} dígitos.`;
      return null;
    }
    case "telefono": {
      const limpio = v.replace(/[\s+\-]/g, "");
      if (!/^\d+$/.test(limpio)) return "Solo se permiten números, espacios y guiones.";
      const min = campo.min ?? 6;
      if (limpio.length < min) return `Debe tener al menos ${min} dígitos.`;
      if (campo.max !== undefined && limpio.length > campo.max)
        return `Debe tener como máximo ${campo.max} dígitos.`;
      return null;
    }
    case "decimal": {
      if (!/^\d+([.,]\d+)?$/.test(v)) return "Debe ser un número (ej.: 1250.50).";
      return null;
    }
    case "cuit": {
      if (!/^\d{11}$/.test(v)) return "El CUIT/CUIL debe tener 11 dígitos.";
      if (!verificarCuit(v)) return "El dígito verificador del CUIT/CUIL no es válido.";
      return null;
    }
    case "email": {
      if (!EMAIL_RE.test(v)) return "El email no es válido.";
      return null;
    }
    case "date": {
      if (!/^\d{4}-\d{2}-\d{2}$/.test(v)) return "Ingresá una fecha válida.";
      const fecha = new Date(`${v}T00:00:00`);
      if (Number.isNaN(fecha.getTime()) || fecha.toISOString().slice(0, 10) !== v)
        return "La fecha no es válida.";
      return null;
    }
    case "periodo": {
      if (!/^\d{4}-\d{2}$/.test(v)) return "Usá el formato AAAA-MM (ej.: 2026-01).";
      const mes = Number(v.slice(5, 7));
      if (mes < 1 || mes > 12) return "El mes debe estar entre 01 y 12.";
      return null;
    }
    case "password": {
      const min = campo.min ?? 6;
      if (v.length < min) return `Debe tener al menos ${min} caracteres.`;
      return null;
    }
    case "select":
      return null;
    default: {
      if (campo.max !== undefined && v.length > campo.max)
        return `Debe tener como máximo ${campo.max} caracteres.`;
      if (campo.min !== undefined && v.length < campo.min)
        return `Debe tener al menos ${campo.min} caracteres.`;
      return null;
    }
  }
}

// Arma el payload a enviar al backend a partir de los valores del formulario.
export function toPayload(
  campos: ReglaCampo[],
  valores: Record<string, string>
): Record<string, unknown> {
  const payload: Record<string, unknown> = {};
  for (const c of campos) {
    const raw = (valores[c.name] ?? "").trim();
    if (raw === "") {
      payload[c.name] = null;
      continue;
    }
    switch (c.tipo) {
      case "select":
        payload[c.name] = /^-?\d+$/.test(raw) ? Number(raw) : raw;
        break;
      case "decimal":
        payload[c.name] = raw.replace(",", ".");
        break;
      case "text": {
        const texto = (valores[c.name] ?? "").trim();
        payload[c.name] = texto || null;
        break;
      }
      default:
        payload[c.name] = raw;
    }
  }
  return payload;
}
