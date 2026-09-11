interface EmptyStateProps {
  titulo: string;
  descripcion?: string;
  accion?: React.ReactNode;
}

export function EmptyState({ titulo, descripcion, accion }: EmptyStateProps) {
  return (
    <div className="flex flex-col items-start gap-2 border border-dashed border-filete px-6 py-10">
      <p className="text-sm font-medium text-tinta">{titulo}</p>
      {descripcion && <p className="text-sm text-neutro">{descripcion}</p>}
      {accion && <div className="mt-2">{accion}</div>}
    </div>
  );
}

export function ErrorState({ mensaje, onReintentar }: { mensaje: string; onReintentar: () => void }) {
  return (
    <div className="flex flex-col items-start gap-2 border border-linea-baja/30 bg-linea-baja/5 px-6 py-10">
      <p className="text-sm font-medium text-linea-baja">No se pudo cargar la información.</p>
      <p className="text-sm text-tinta">{mensaje}</p>
      <button
        onClick={onReintentar}
        className="mt-2 text-sm font-medium text-tinta underline underline-offset-2"
      >
        Reintentar
      </button>
    </div>
  );
}
