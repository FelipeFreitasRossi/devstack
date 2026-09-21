import { createContext, useContext, useState, useEffect } from 'react';
import type { ReactNode } from 'react';
import { api } from '../services/api';

interface User {
  id: string;
  name: string;
  email: string;
  paid: boolean;
}

// Cadastro que ainda NÃO está no banco: fica só na memória até o pagamento ser confirmado.
interface PendingSignup {
  name: string;
  email: string;
  password: string; // só em memória (some ao recarregar a página); nunca vai para o localStorage
  signupToken: string;
}

interface AuthContextType {
  user: User | null;
  loading: boolean;
  pendingSignup: PendingSignup | null;
  login: (email: string, password: string) => Promise<void>;
  register: (name: string, email: string, password: string) => Promise<void>;
  completeSignup: (data: { access_token: string; user: User }) => void;
  logout: () => void;
  updateUser: (user: User) => void;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [pendingSignup, setPendingSignup] = useState<PendingSignup | null>(null);

  // Restaura sessão ao carregar
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      setLoading(false);
      return;
    }

    api
      .me()
      .then((data) => setUser(data as User))
      .catch(() => {
        localStorage.removeItem('token');
        setUser(null);
      })
      .finally(() => setLoading(false));
  }, []);

  const login = async (email: string, password: string) => {
    const data = (await api.login(email, password)) as {
      access_token: string;
      user: User;
    };
    localStorage.setItem('token', data.access_token);
    setUser(data.user);
    setPendingSignup(null);
  };

  // Não cria conta nem faz login: só valida os dados e guarda em memória.
  // A conta só passa a existir depois do pagamento confirmado (completeSignup).
  const register = async (name: string, email: string, password: string) => {
    const data = (await api.register(name, email, password)) as {
      signup_token: string;
    };
    setPendingSignup({ name, email, password, signupToken: data.signup_token });
  };

  // Chamada quando o pagamento é confirmado e o backend já criou o usuário.
  const completeSignup = (data: { access_token: string; user: User }) => {
    localStorage.setItem('token', data.access_token);
    setUser(data.user);
    setPendingSignup(null);
  };

  const logout = () => {
    localStorage.removeItem('token');
    setUser(null);
  };

  const updateUser = (updated: User) => setUser(updated);

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        pendingSignup,
        login,
        register,
        completeSignup,
        logout,
        updateUser,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth deve ser usado dentro de AuthProvider');
  }
  return context;
}