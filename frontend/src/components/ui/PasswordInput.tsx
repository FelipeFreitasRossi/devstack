import { forwardRef, useId, useState } from 'react';
import type { InputHTMLAttributes } from 'react';
import { Eye, EyeOff } from 'lucide-react';

interface PasswordInputProps extends InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
}

/**
 * Campo de senha com botão de olho para mostrar/ocultar o valor digitado.
 * Reaproveita o mesmo visual do componente Input e os ícones (lucide-react)
 * já usados no restante do projeto.
 */
export const PasswordInput = forwardRef<HTMLInputElement, PasswordInputProps>(
  ({ label, error, className = '', id, ...props }, ref) => {
    const autoId = useId();
    const inputId = id || props.name || autoId;
    const [visible, setVisible] = useState(false);

    return (
      <div className="w-full">
        {label && (
          <label
            htmlFor={inputId}
            className="block text-sm font-medium text-text-secondary mb-2"
          >
            {label}
          </label>
        )}

        <div className="relative">
          <input
            ref={ref}
            id={inputId}
            type={visible ? 'text' : 'password'}
            className={`
              w-full px-4 py-3 pr-12 rounded-lg
              bg-surface-elevated border border-border
              text-text-primary placeholder:text-text-muted
              transition-colors duration-200
              focus:outline-none focus:border-brand-500 focus:ring-1 focus:ring-brand-500/50
              disabled:opacity-50 disabled:cursor-not-allowed
              ${error ? 'border-danger focus:border-danger focus:ring-danger/50' : ''}
              ${className}
            `}
            {...props}
          />

          <button
            type="button"
            onClick={() => setVisible((v) => !v)}
            className="absolute inset-y-0 right-0 flex items-center justify-center w-11 text-text-muted hover:text-text-primary transition-colors focus:outline-none focus-visible:text-brand-500"
            aria-label={visible ? 'Ocultar senha' : 'Mostrar senha'}
            aria-pressed={visible}
            tabIndex={-1}
          >
            {visible ? <EyeOff size={18} /> : <Eye size={18} />}
          </button>
        </div>

        {error && <p className="mt-1.5 text-xs text-danger">{error}</p>}
      </div>
    );
  }
);

PasswordInput.displayName = 'PasswordInput';
