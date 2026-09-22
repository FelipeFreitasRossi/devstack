# DevStack — Plataforma Saas Full Stack

Plataforma completa de cursos online, com backend em FastAPI, frontend em React + TypeScript e banco de dados MongoDB. Sistema de autenticação com JWT, painel do aluno, progresso de aulas, conquistas, integração com Mercado Pago e deploy em produção.

🌐 **Produção:** [https://inteligenciabrasileira.com](https://inteligenciabrasileira.com)
📚 **API Docs:** [https://devstack-z0gf.onrender.com/docs](https://devstack-z0gf.onrender.com/docs)

---

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Stack Tecnológica](#-stack-tecnológica)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Funcionalidades](#-funcionalidades)
- [Como Rodar Localmente](#-como-rodar-localmente)
- [Variáveis de Ambiente](#-variáveis-de-ambiente)
- [API — Endpoints Principais](#-api--endpoints-principais)
- [Deploy](#-deploy)
- [Arquitetura](#-arquitetura)
- [Segurança](#-segurança)
- [Roadmap](#-roadmap)
- [Licença](#-licença)

---

## 🎯 Visão Geral

O **DevStack** é uma plataforma de ensino de programação com foco em full stack. O aluno percorre uma trilha de módulos (Lógica de Programação, Python, FastAPI, Git/GitHub, Deploy), com aulas teóricas, exercícios de código corrigidos automaticamente em sandbox Python, sistema de progresso, conquistas e integração de pagamento.

**Principais usuários:**
- **Aluno:** consome o conteúdo, faz exercícios, acompanha progresso.
- **Admin:** gerencia módulos, aulas e usuários.

---

## 🛠 Stack Tecnológica

### Backend
- **Python 3.14**
- **FastAPI** — framework web moderno e assíncrono
- **Uvicorn** — servidor ASGI
- **Pydantic** — validação de dados
- **PyMongo** — driver oficial do MongoDB
- **python-jose** — geração e validação de JWT
- **bcrypt** — hash de senhas
- **python-dotenv** — gestão de variáveis de ambiente
- **Mercado Pago SDK** — integração de pagamentos

### Frontend
- **React 18** + **TypeScript**
- **Vite** — build tool ultrarrápido
- **Tailwind CSS** — estilização
- **React Router** — roteamento SPA
- **GSAP** — animações
- **Lucide React** — ícones

### Banco de Dados
- **MongoDB Atlas** — banco NoSQL na nuvem (plano M0 gratuito)

### Infraestrutura
- **Render** — hospedagem do backend (plano Free)
- **HostGator** — hospedagem do frontend estático (cPanel)
- **UptimeRobot** — monitoramento anti-sleep
- **GitHub** — versionamento de código
