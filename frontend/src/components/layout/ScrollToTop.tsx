import { useLayoutEffect } from 'react';
import { useLocation } from 'react-router-dom';

// Páginas que devem abrir sempre no começo (Termos, Privacidade, Reembolso)
const PAGES_FROM_TOP = ['/termos', '/privacidade', '/reembolso'];

export function ScrollToTop() {
  const { pathname } = useLocation();

  useLayoutEffect(() => {
    if (PAGES_FROM_TOP.includes(pathname)) {
      // 'instant' ignora o scroll suave do CSS: vai direto para o topo, sem "descer/subir" a página
      window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
    }
  }, [pathname]);

  return null;
}
