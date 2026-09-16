import {
  createContext,
  useCallback,
  useContext,
  useRef,
  useState,
} from 'react';
import type { ReactNode } from 'react';
import { useNavigate } from 'react-router-dom';
import gsap from 'gsap';

type Direction = 'from-left' | 'from-right';

interface AuthTransitionContextValue {
  containerRef: React.RefObject<HTMLDivElement | null>;
  direction: Direction;
  setDirection: (d: Direction) => void;
  goToLogin: () => void;
  goToCadastro: () => void;
}

const AuthTransitionContext =
  createContext<AuthTransitionContextValue | null>(null);

export function AuthTransitionProvider({ children }: { children: ReactNode }) {
  const containerRef = useRef<HTMLDivElement>(null);
  const navigate = useNavigate();
  const [direction, setDirection] = useState<Direction>('from-right');

  const transitionTo = useCallback(
    (path: string, exitX: number, nextDirection: Direction) => {
      const el = containerRef.current;
      if (!el) {
        setDirection(nextDirection);
        navigate(path);
        return;
      }

      // Anima a tela atual saindo
      gsap.to(el, {
        x: exitX,
        opacity: 0,
        duration: 0.45,
        ease: 'power2.in',
        onComplete: () => {
          // Seta a direção da próxima tela e navega
          setDirection(nextDirection);
          navigate(path);
        },
      });
    },
    [navigate]
  );

  // Login → Cadastro: Login sai pela ESQUERDA, Cadastro entra da DIREITA
  const goToCadastro = useCallback(
    () => transitionTo('/cadastro', -320, 'from-right'),
    [transitionTo]
  );

  // Cadastro → Login: Cadastro sai pela DIREITA, Login entra da ESQUERDA
  const goToLogin = useCallback(
    () => transitionTo('/login', 320, 'from-left'),
    [transitionTo]
  );

  return (
    <AuthTransitionContext.Provider
      value={{
        containerRef,
        direction,
        setDirection,
        goToLogin,
        goToCadastro,
      }}
    >
      {children}
    </AuthTransitionContext.Provider>
  );
}

export function useAuthTransition() {
  const ctx = useContext(AuthTransitionContext);
  if (!ctx) {
    throw new Error(
      'useAuthTransition deve ser usado dentro de AuthTransitionProvider'
    );
  }
  return ctx;
}