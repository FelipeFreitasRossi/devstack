import { useState } from 'react';
import { Save, X, Pencil, Loader2, CheckCircle2, User, Mail, Lock as LockIcon } from 'lucide-react';
import { Button } from '../ui/Button';

interface ProfileInfoProps {
  name: string;
  email: string;
  onSaveName: (name: string) => Promise<void>;
}

export function ProfileInfo({ name, email, onSaveName }: ProfileInfoProps) {
  const [isEditing, setIsEditing] = useState(false);
  const [draftName, setDraftName] = useState(name);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  const handleSave = async () => {
    setError('');
    const trimmed = draftName.trim();

    if (trimmed.length < 2) {
      setError('O nome deve ter pelo menos 2 caracteres');
      return;
    }

    if (trimmed === name) {
      setIsEditing(false);
      return;
    }

    setSaving(true);
    try {
      await onSaveName(trimmed);
      setSuccess(true);
      setIsEditing(false);
      setTimeout(() => setSuccess(false), 3000);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Erro ao salvar');
    } finally {
      setSaving(false);
    }
  };

  const handleCancel = () => {
    setDraftName(name);
    setIsEditing(false);
    setError('');
  };

  return (
    <section>
      <div className="flex items-center gap-2 mb-4">
        <User size={16} className="text-brand-500" />
        <h2 className="text-lg md:text-xl font-bold text-text-primary">
          Dados pessoais
        </h2>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {/* Nome */}
        <div
          className={`rounded-xl border bg-surface-elevated p-5 transition-colors ${
            isEditing ? 'sm:col-span-2 border-brand-500/40' : 'border-border hover:border-border-strong'
          }`}
        >
          <div className="flex items-center gap-2 mb-3">
            <User size={13} className="text-text-muted" />
            <label className="text-xs font-medium text-text-secondary uppercase tracking-wider">
              Nome completo
            </label>
          </div>

          {isEditing ? (
            <div className="flex flex-col sm:flex-row gap-2">
              <input
                type="text"
                value={draftName}
                onChange={(e) => setDraftName(e.target.value)}
                disabled={saving}
                className="flex-1 px-4 py-2.5 rounded-lg bg-surface border border-border text-text-primary focus:outline-none focus:border-brand-500 transition-colors disabled:opacity-50"
                autoFocus
              />
              <div className="flex gap-2">
                <Button
                  onClick={handleSave}
                  disabled={saving}
                  size="md"
                  className="flex-1 sm:flex-none"
                >
                  {saving ? (
                    <>
                      <Loader2 size={16} className="animate-spin" />
                      Salvando
                    </>
                  ) : (
                    <>
                      <Save size={16} />
                      Salvar
                    </>
                  )}
                </Button>
                <button
                  onClick={handleCancel}
                  disabled={saving}
                  className="p-2.5 rounded-lg border border-border text-text-secondary hover:text-text-primary hover:border-border-strong transition-colors disabled:opacity-50"
                  aria-label="Cancelar"
                >
                  <X size={18} />
                </button>
              </div>
            </div>
          ) : (
            <div className="flex items-center justify-between gap-3">
              <span className="text-text-primary font-medium truncate">{name}</span>
              <button
                onClick={() => setIsEditing(true)}
                className="shrink-0 inline-flex items-center gap-1.5 text-xs text-brand-500 hover:text-brand-400 font-medium transition-colors"
              >
                <Pencil size={12} />
                Editar
              </button>
            </div>
          )}

          {error && <p className="text-xs text-danger mt-2">{error}</p>}
          {success && (
            <p className="text-xs text-accent-500 mt-2 inline-flex items-center gap-1.5">
              <CheckCircle2 size={12} />
              Nome atualizado
            </p>
          )}
        </div>

        {/* Email (read-only) */}
        {!isEditing && (
          <div className="rounded-xl border border-border bg-surface-elevated p-5 hover:border-border-strong transition-colors">
            <div className="flex items-center gap-2 mb-3">
              <Mail size={13} className="text-text-muted" />
              <label className="text-xs font-medium text-text-secondary uppercase tracking-wider">
                Email
              </label>
            </div>
            <div className="flex items-center justify-between gap-3">
              <span className="text-text-primary font-medium truncate">{email}</span>
              <span className="shrink-0 inline-flex items-center gap-1 text-xs text-text-muted">
                <LockIcon size={11} />
              </span>
            </div>
            <p className="text-xs text-text-muted mt-2">
              O email não pode ser alterado.
            </p>
          </div>
        )}
      </div>
    </section>
  );
}