import { useState } from "react";
import type { ColumnDef } from "@tanstack/react-table";
import { DataTable } from "../../components/ui/DataTable";
import { SlideOver } from "../../components/ui/SlideOver";
import { Button } from "../../components/ui/Button";
import { TextField, SelectField } from "../../components/ui/Field";
import { EmptyState, ErrorState } from "../../components/ui/EmptyState";
import { useToast } from "../../components/ui/Toast";
import { ApiError } from "../../lib/api";
import { useFormulario } from "../../lib/useFormulario";
import { toPayload, type ReglaCampo } from "../../lib/validation";
import { useCrudMutations, useRoles, useUsuarios } from "../../lib/queries";
import type { Usuario } from "../../lib/types";

const REGLAS: ReglaCampo[] = [
  { name: "username", label: "Usuario", tipo: "text", required: true, max: 80 },
  { name: "email", label: "Email", tipo: "email", required: true, max: 150 },
  { name: "password", label: "Contraseña", tipo: "password", required: true, min: 6 },
  { name: "rol_id", label: "Rol", tipo: "select", required: true },
];

export function UsuariosPage() {
  const usuarios = useUsuarios();
  const roles = useRoles();
  const { crear, actualizar } = useCrudMutations<Usuario>("usuarios", "/usuarios");
  const { mostrar } = useToast();

  const [panel, setPanel] = useState(false);
  const { valores, errores, setValor, setValores, setValoresDesde, validarTodos, validarUno } = useFormulario(REGLAS);

  const columnas: ColumnDef<Usuario, any>[] = [
    { header: "Usuario", accessorKey: "username", cell: (c) => <span className="dato">{c.getValue()}</span> },
    { header: "Email", accessorKey: "email" },
    { header: "Rol", accessorFn: (u) => u.rol.nombre },
    {
      header: "Activo",
      accessorKey: "activo",
      cell: (c) => (c.getValue() ? <span className="text-linea-ok">Sí</span> : <span className="text-linea-baja">No</span>),
    },
  ];

  async function alternarActivo(u: Usuario) {
    try {
      await actualizar.mutateAsync({
        id: u.id,
        payload: { username: u.username, email: u.email, rol_id: u.rol.id, activo: !u.activo },
      });
      mostrar(u.activo ? "Usuario desactivado." : "Usuario activado.");
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo actualizar.", "error");
    }
  }

  async function guardar() {
    if (!validarTodos()) {
      mostrar("Revisá los campos marcados en rojo.", "error");
      return;
    }
    try {
      await crear.mutateAsync(toPayload(REGLAS, valores));
      mostrar("Usuario creado.");
      setPanel(false);
      setValoresDesde(null);
    } catch (err) {
      mostrar(err instanceof ApiError ? err.detail : "No se pudo crear el usuario.", "error");
    }
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h1 className="text-lg font-semibold text-tinta">Usuarios</h1>
        <Button variant="primario" onClick={() => { setValoresDesde(null); setPanel(true); }}>Crear usuario</Button>
      </div>

      {usuarios.isLoading && <EmptyState titulo="Cargando…" />}
      {usuarios.isError && <ErrorState mensaje={(usuarios.error as Error)?.message ?? ""} onReintentar={() => usuarios.refetch()} />}
      {!usuarios.isLoading && !usuarios.isError && (
        <DataTable
          columns={columnas}
          data={usuarios.data ?? []}
          onEditar={alternarActivo}
          vacioTitulo="Todavía no hay usuarios cargados."
        />
      )}
      <p className="text-xs text-neutro">El enlace “Editar” de cada fila activa o desactiva ese usuario.</p>

      <SlideOver
        abierto={panel}
        titulo="Crear usuario"
        onCerrar={() => setPanel(false)}
        footer={
          <div className="flex justify-end gap-2">
            <Button variant="texto" onClick={() => setPanel(false)}>Cancelar</Button>
            <Button variant="primario" onClick={guardar}>Crear</Button>
          </div>
        }
      >
        <div className="space-y-4">
          <TextField label="Usuario" required dato maxLength={80} value={valores.username ?? ""} error={errores.username} onChange={(e) => setValor("username", e.target.value)} onBlur={() => validarUno("username")} />
          <TextField label="Email" required type="email" maxLength={150} value={valores.email ?? ""} error={errores.email} onChange={(e) => setValor("email", e.target.value)} onBlur={() => validarUno("email")} />
          <TextField label="Contraseña" required type="password" value={valores.password ?? ""} error={errores.password} onChange={(e) => setValor("password", e.target.value)} onBlur={() => validarUno("password")} />
          <SelectField
            label="Rol"
            required
            options={(roles.data ?? []).map((r) => ({ value: r.id, label: r.nombre }))}
            value={valores.rol_id ?? ""}
            error={errores.rol_id}
            onChange={(e) => setValor("rol_id", e.target.value)}
          />
        </div>
      </SlideOver>
    </div>
  );
}
