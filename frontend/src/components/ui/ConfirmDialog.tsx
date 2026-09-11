import { Button } from "./Button";

interface ConfirmDialogProps {
  abierto: boolean;
  titulo: string;
  descripcion: string;
  textoConfirmar?: string;
  onConfirmar: () => void;
  onCancelar: () => void;
}

export function ConfirmDialog({
  abierto,
  titulo,
  descripcion,
  textoConfirmar = "Eliminar",
  onConfirmar,
  onCancelar,
}: ConfirmDialogProps) {
  if (!abierto) return null;
  return (
    <div className="fixed inset-0 z-40 flex items-center justify-center">
      <div className="absolute inset-0 bg-tinta/30" onClick={onCancelar} />
      <div className="relative w-full max-w-sm border border-filete bg-papel-alto p-5">
        <h2 className="text-base font-semibold text-tinta">{titulo}</h2>
        <p className="mt-2 text-sm text-neutro">{descripcion}</p>
        <div className="mt-5 flex justify-end gap-2">
          <Button variant="texto" onClick={onCancelar}>
            Cancelar
          </Button>
          <Button variant="destructivo" onClick={onConfirmar}>
            {textoConfirmar}
          </Button>
        </div>
      </div>
    </div>
  );
}
