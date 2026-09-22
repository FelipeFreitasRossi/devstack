import { createContext, useContext, useState, useEffect } from 'react';
import type { ReactNode } from 'react';
import { api } from '../services/api';

interface User {
  id: string;
  name: string;
  email: string;
  paid: boolean;
}

interface PendingSignup {
  name: string;
  email: string;
  password?: string;
  signupToken: string;
}

type PersistedPendingSignup = Omit<PendingSignup, 'password'>;

const PENDING_SIGNUP_KEY = 'pending_signup';

function loadPendingSignup(): PendingSignup | null {
  try {
    const raw = sessionStorage.getItem(PENDING_SIGNUP_KEY);
    if (!raw) return null;
    return JSON.parse(raw) as PersistedPendingSignup;
  } catch {
    return null;
  }
}

function persistPendingSignup(data: PendingSignup | null): void {
  try {
    if (data) {
      const { name, email, signupToken } = data;
      sessionStorage.setItem(
        PENDING_SIGNUP_KEY,
        JSON.stringify({ name, email, signupToken })
      );
    } else {
      sessionStorage.removeItem(PENDING_SIGNUP_KEY);
    }
  } catch {
    // sessionStorage indisponível (raro); segue só em memória
  }
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

  const [pendingSignup, setPendingSignupState] = useState<PendingSignup | null>(
    () => loadPendingSignup()
  );

  const setPendingSignup = (data: PendingSignup | null) => {
    setPendingSignupState(data);
    persistPendingSignup(data);
  };

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

  const register = async (name: string, email: string, password: string) => {
    const data = (await api.register(name, email, password)) as {
      signup_token: string;
    };
    setPendingSignup({
      name,
      email,
      password,
      signupToken: data.signup_token,
    });
  };

  const completeSignup = (data: { access_token: string; user: User }) => {
    localStorage.setItem('token', data.access_token);
    setUser(data.user);
    setPendingSignup(null);
  };

  const logout = () => {
    localStorage.removeItem('token');
    setUser(null);
    setPendingSignup(null);
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