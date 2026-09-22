import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  QrCode,
  Copy,
  Check,
  Loader2,
  AlertCircle,
  ArrowLeft,
} from 'lucide-react';
import { AuthLayout } from '../components/layout/AuthLayout.tsx';
import { Button } from '../components/ui/Button';
import { useAuth } from '../contexts/AuthContext';
import { api } from '../services/api';

type PaymentMethod = 'pix';

interface SignupCompleted {
  paid: boolean;
  access_token?: string;
  user?: {
    id: string;
    name: string;
    email: string;
    paid: boolean;
  };
}

interface PaymentData {
  order_id: string;
  method: PaymentMethod;
  qr_code?: string;
  qr_code_base64?: string;
  ticket_url?: string;
}

async function copyToClipboard(text: string): Promise<boolean> {
  if (navigator.clipboard && window.isSecureContext) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch {
      // Cai no fallback
    }
  }

  try {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.top = '-9999px';
    document.body.appendChild(textarea);
    textarea.focus();
    textarea.select();
    const success = document.execCommand('copy');
    document.body.removeChild(textarea);
    return success;
  } catch {
    return false;
  }
}

function BackButton({ onClick, label }: { onClick: () => void; label: string }) {
  return (
    <button
      type="button"
      onClick={onClick}
      aria-label={label}
      className="inline-flex items-center gap-1.5 -ml-1 px-1 py-1 rounded-md text-sm text-text-muted hover:text-text-primary focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-500 transition-colors"
    >
      <ArrowLeft size={18} />
      Voltar
    </button>
  );
}

export function Checkout() {
  const navigate = useNavigate();
  const {
    user,
    loading: authLoading,
    updateUser,
    pendingSignup,
    completeSignup,
  } = useAuth();
  const signupToken = pendingSignup?.signupToken;
  const [payment, setPayment] = useState<PaymentData | null>(null);
  const [selectedMethod] = useState<PaymentMethod>('pix');
  const [loading, setLoading] = useState(false);
  const [copied, setCopied] = useState(false);
  const [copyError, setCopyError] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (user?.paid && !pendingSignup) {
      navigate('/minha-area');
    }
  }, [user, pendingSignup, navigate]);

  useEffect(() => {
    if (!authLoading && !user && !pendingSignup && !localStorage.getItem('token')) {
      navigate('/cadastro');
    }
  }, [authLoading, user, pendingSignup, navigate]);

  useEffect(() => {
    if (!payment?.order_id) return;

    const interval = setInterval(async () => {
      try {
        const result = (await api.checkPaymentStatus(
          payment.order_id,
          signupToken
        )) as SignupCompleted;
        if (result.paid && signupToken && result.access_token && result.user) {
          completeSignup({
            access_token: result.access_token,
            user: result.user,
          });
          navigate('/minha-area');
        } else if (result.paid && user) {
          updateUser({ ...user, paid: true });
          navigate('/minha-area');
        }
      } catch {
        // Silencia erros do polling
      }
    }, 5000);

    return () => clearInterval(interval);
  }, [payment, user, signupToken, updateUser, completeSignup, navigate]);

  const handleGeneratePayment = async () => {
    if (!signupToken && !user && !localStorage.getItem('token')) {
      setError('Você precisa fazer login ou refazer o cadastro para continuar.');
      return;
    }

    setLoading(true);
    setError('');
    try {
      const data = (await api.createPayment(
        selectedMethod,
        signupToken
      )) as PaymentData;
      setPayment(data);
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : 'Erro ao gerar pagamento. Tente novamente.'
      );
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = async (text: string | undefined) => {
    if (!text) return;
    setCopyError(false);
    const success = await copyToClipboard(text);

    if (success) {
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } else {
      setCopyError(true);
      setTimeout(() => setCopyError(false), 3000);
    }
  };

  const resetMethod = () => {
    setPayment(null);
    setError('');
  };

  const handleBackToCadastro = () => navigate('/cadastro');

  if (authLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-surface">
        <Loader2 size={32} className="text-brand-500 animate-spin" />
      </div>
    );
  }

  if (!payment) {
    return (
      <AuthLayout
        title="Finalize sua compra"
        subtitle="Acesso vitalício por apenas R$19,99"
        scrollable
      >
        <div className="space-y-4 sm:space-y-6">
          {pendingSignup && (
            <div className="-mb-2">
              <BackButton
                onClick={handleBackToCadastro}
                label="Voltar para o cadastro"
              />
            </div>
          )}

          <div className="text-center py-2 sm:py-6">
            <div className="text-4xl sm:text-5xl font-bold text-brand-500 mb-2">
              R$ 19,99
            </div>
            <p className="text-text-secondary text-sm">
              Pagamento único · Acesso vitalício
            </p>
          </div>

          <div className="space-y-2 text-sm text-text-secondary">
            <div className="flex items-center gap-2">
              <Check size={16} className="text-brand-500" />
              Acesso a todos os módulos
            </div>
            <div className="flex items-center gap-2">
              <Check size={16} className="text-brand-500" />
              Atualizações para sempre
            </div>
            <div className="flex items-center gap-2">
              <Check size={16} className="text-brand-500" />
              Comunidade exclusiva
            </div>
          </div>

          <div className="p-4 rounded-lg border border-brand-500 bg-brand-500/10 text-center">
            <QrCode size={22} className="mx-auto mb-2 text-brand-500" />
            <span className="text-sm font-medium text-brand-500">
              Pagamento via Pix
            </span>
            <p className="text-xs text-text-muted mt-1">
              QR Code gerado na hora
            </p>
          </div>

          {error && (
            <div className="p-3 rounded-lg bg-danger/10 border border-danger/30 flex items-start gap-2">
              <AlertCircle size={16} className="text-danger shrink-0 mt-0.5" />
              <p className="text-danger text-sm">{error}</p>
            </div>
          )}

          <Button
            onClick={handleGeneratePayment}
            size="lg"
            className="w-full"
            disabled={loading}
          >
            {loading ? (
              <>
                <Loader2 size={18} className="animate-spin" />
                Gerando...
              </>
            ) : (
              <>Gerar pagamento via Pix</>
            )}
          </Button>

          <p className="text-center text-xs text-text-muted">
            Pagamento seguro · Mercado Pago
          </p>
        </div>
      </AuthLayout>
    );
  }

  return (
    <AuthLayout
      title="Aguardando pagamento"
      subtitle="Finalize o pagamento para liberar o acesso"
      scrollable
    >
      <div className="space-y-4 sm:space-y-6">
        <div className="-mb-1">
          <BackButton
            onClick={resetMethod}
            label="Voltar para a escolha da forma de pagamento"
          />
        </div>

        {payment?.qr_code_base64 && (
          <div className="text-center">
            <p className="text-sm text-text-secondary mb-3 sm:mb-4">
              Escaneie o QR Code com o app do seu banco
            </p>
            <div className="bg-white p-3 sm:p-4 rounded-xl inline-block">
              <img
                src={`data:image/png;base64,${payment.qr_code_base64}`}
                alt="QR Code Pix"
                className="w-40 h-40 sm:w-48 sm:h-48 md:w-56 md:h-56"
              />
            </div>
          </div>
        )}

        <div className="flex items-center gap-3">
          <div className="flex-1 h-px bg-border" />
          <span className="text-xs text-text-muted uppercase tracking-wider">
            ou
          </span>
          <div className="flex-1 h-px bg-border" />
        </div>

        <div>
          <p className="text-sm text-text-secondary mb-3 text-center">
            Copie o código e pague pelo app do banco
          </p>

          {payment?.qr_code && (
            <div className="mb-3">
              <div className="p-3 rounded-lg bg-surface border border-border max-h-20 sm:max-h-none overflow-y-auto">
                <code className="block text-[10px] text-text-muted break-all font-mono leading-relaxed">
                  {payment.qr_code}
                </code>
              </div>
            </div>
          )}

          <button
            onClick={() => handleCopy(payment?.qr_code)}
            className={`w-full p-3 sm:p-4 rounded-lg border transition-all duration-200 flex items-center justify-center gap-2 ${
              copied
                ? 'bg-brand-500/10 border-brand-500'
                : copyError
                ? 'bg-danger/10 border-danger'
                : 'bg-surface border-border hover:border-brand-500/50'
            }`}
          >
            {copied ? (
              <>
                <Check size={18} className="text-brand-500" />
                <span className="text-brand-500 font-medium">
                  Código copiado!
                </span>
              </>
            ) : copyError ? (
              <>
                <AlertCircle size={18} className="text-danger" />
                <span className="text-danger font-medium">
                  Não foi possível copiar
                </span>
              </>
            ) : (
              <>
                <Copy size={18} className="text-brand-500" />
                <span className="text-text-primary font-medium">
                  Copiar código Pix
                </span>
              </>
            )}
          </button>

          {copyError && (
            <p className="text-xs text-text-muted mt-2 text-center">
              Selecione o código acima manualmente e copie
            </p>
          )}
        </div>

        <div className="p-3 sm:p-4 rounded-lg bg-surface border border-border text-center">
          <p className="text-xs text-text-muted mb-1">Valor a pagar</p>
          <p className="text-2xl font-bold text-brand-500">R$ 19,99</p>
          <p className="text-xs text-text-muted mt-1">
            Valor fixo definido pelo vendedor
          </p>
        </div>

        <div className="p-3 rounded-lg bg-brand-500/10 border border-brand-500/30 flex items-center gap-3">
          <Loader2
            size={18}
            className="text-brand-500 animate-spin shrink-0"
          />
          <p className="text-xs text-brand-300">
            Aguardando confirmação do pagamento...
          </p>
        </div>

        <button
          onClick={resetMethod}
          className="w-full text-xs text-text-muted hover:text-text-secondary transition-colors"
        >
          Voltar
        </button>
      </div>
    </AuthLayout>
  );
}