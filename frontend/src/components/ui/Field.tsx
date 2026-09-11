import type { InputHTMLAttributes, ReactNode, SelectHTMLAttributes, TextareaHTMLAttributes } from "react";
import { useState } from "react";
import { Eye, EyeOff } from "lucide-react";

interface FieldWrapperProps {
  label: string;
  error?: string;
  hint?: string;
  children?: ReactNode;
  dato?: boolean;
}

export function FieldWrapper({ label, error, hint, children }: FieldWrapperProps) {
  return (
    <label className="block">
      <span className="mb-1.5 block text-sm font-medium text-tinta">{label}</span>
      {children}
      {hint && !error && <span className="mt-1 block text-xs text-neutro">{hint}</span>}
      {error && <span className="mt-1 block text-xs text-linea-baja">{error}</span>}
    </label>
  );
}

const inputBase =
  "w-full rounded border border-filete bg-papel-alto px-3 py-2 text-sm text-tinta placeholder:text-neutro focus:border-senal";

type InputProps = InputHTMLAttributes<HTMLInputElement> & FieldWrapperProps;

export function TextField({ label, error, hint, dato, className = "", type, ...props }: InputProps) {
  const [showPassword, setShowPassword] = useState(false);
  const isPassword = type === "password";
  const inputType = isPassword && showPassword ? "text" : type;

  return (
    <FieldWrapper label={label} error={error} hint={hint}>
      <div className="relative">
        <input className={`${inputBase} ${dato ? "dato" : ""} ${className}`} type={inputType} {...props} />
        {isPassword && (
          <button
            type="button"
            className="absolute right-3 top-1/2 -translate-y-1/2 text-neutro hover:text-tinta transition-colors"
            onClick={() => setShowPassword(!showPassword)}
            tabIndex={-1}
          >
            {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
          </button>
        )}
      </div>
    </FieldWrapper>
  );
}

type TextareaProps = TextareaHTMLAttributes<HTMLTextAreaElement> & FieldWrapperProps;

export function TextAreaField({ label, error, hint, className = "", ...props }: TextareaProps) {
  return (
    <FieldWrapper label={label} error={error} hint={hint}>
      <textarea className={`${inputBase} min-h-[80px] resize-y ${className}`} {...props} />
    </FieldWrapper>
  );
}

interface SelectProps extends SelectHTMLAttributes<HTMLSelectElement>, Omit<FieldWrapperProps, "children"> {
  options: { value: string | number; label: string }[];
  placeholder?: string;
}

export function SelectField({ label, error, hint, options, placeholder, className = "", ...props }: SelectProps) {
  return (
    <FieldWrapper label={label} error={error} hint={hint}>
      <select className={`${inputBase} ${className}`} {...props}>
        <option value="">{placeholder ?? "Sin asignar"}</option>
        {options.map((o) => (
          <option key={o.value} value={o.value}>
            {o.label}
          </option>
        ))}
      </select>
    </FieldWrapper>
  );
}
