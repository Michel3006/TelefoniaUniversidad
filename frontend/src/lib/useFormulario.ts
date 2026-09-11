import { useCallback, useState } from "react";
import { limpiar, validarCampo, type FormError, type ReglaCampo } from "./validation";

export function useFormulario(campos: ReglaCampo[]) {
  const vacios = useCallback(
    () => Object.fromEntries(campos.map((c) => [c.name, ""])),
    [campos]
  );
  const [valores, setValores] = useState<Record<string, string>>(vacios);
  const [errores, setErrores] = useState<FormError>({});

  // Actualiza un campo aplicando la limpieza según su tipo y borra su error.
  const setValor = (name: string, raw: string) => {
    const campo = campos.find((c) => c.name === name);
    if (!campo) return;
    setValores((v) => ({ ...v, [name]: limpiar(campo.tipo, raw) }));
    setErrores((e) => {
      const copia = { ...e };
      delete copia[name];
      return copia;
    });
  };

  // Llena el formulario desde un registro existente (o lo vacía con `null`).
  const setValoresDesde = (item: object | null) => {
    const registro = (item ?? {}) as Record<string, unknown>;
    const out: Record<string, string> = {};
    for (const c of campos) {
      const valor = registro[c.name];
      out[c.name] = valor === null || valor === undefined ? "" : String(valor);
    }
    setValores(out);
    setErrores({});
  };

  const validarUno = (name: string): string | null => {
    const campo = campos.find((c) => c.name === name);
    if (!campo) return null;
    const error = validarCampo(valores[name] ?? "", campo);
    setErrores((e) => {
      const copia = { ...e };
      if (error) copia[name] = error;
      else delete copia[name];
      return copia;
    });
    return error;
  };

  const validarTodos = (): boolean => {
    const e: FormError = {};
    for (const c of campos) {
      const error = validarCampo(valores[c.name] ?? "", c);
      if (error) e[c.name] = error;
    }
    setErrores(e);
    return Object.keys(e).length === 0;
  };

  const marcarError = (name: string, mensaje: string | null) => {
    setErrores((e) => {
      const copia = { ...e };
      if (mensaje) copia[name] = mensaje;
      else delete copia[name];
      return copia;
    });
  };

  return { valores, errores, setValor, setValores, setValoresDesde, validarUno, validarTodos, marcarError };
}