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

## 📁 Estrutura do Projeto
devstack/
├── backend/ # API FastAPI
│ ├── app/
│ │ ├── main.py # Ponto de entrada FastAPI
│ │ ├── database.py # Conexão MongoDB
│ │ ├── auth.py # Autenticação JWT + bcrypt
│ │ ├── analytics.py # CURRICULUM + cálculos de progresso
│ │ ├── models.py # Schemas Pydantic
│ │ ├── lessons_content/ # Conteúdo das aulas (modularizado)
│ │ │ ├── init.py
│ │ │ ├── lessons_module_01.py
│ │ │ ├── lessons_module_02.py
│ │ │ └── ...
│ │ └── routes/ # Rotas da API
│ │ ├── auth.py
│ │ ├── lessons.py
│ │ ├── dashboard.py
│ │ ├── profile.py
│ │ ├── payments.py
│ │ └── webhooks.py
│ ├── requirements.txt
│ └── .env.example
│
├── frontend/ # App React + TypeScript
│ ├── src/
│ │ ├── components/ # Componentes reutilizáveis
│ │ ├── pages/ # Páginas (rotas)
│ │ ├── services/ # Chamadas à API
│ │ ├── contexts/ # Context API (auth, etc)
│ │ ├── hooks/ # Custom hooks
│ │ └── styles/
│ ├── public/
│ ├── package.json
│ ├── vite.config.ts
│ └── .env.example
│
└── README.md

---

## ✨ Funcionalidades

### 👤 Autenticação
- [x] Cadastro com validação de email e senha forte
- [x] Login com JWT (expiração de 24h)
- [x] Hash de senhas com bcrypt
- [x] Rotas protegidas via `Depends()`
- [x] Refresh de token

### 📚 Conteúdo
- [x] 8 módulos com aulas teóricas e exercícios
- [x] Conteúdo das aulas em arquivos modulares Python
- [x] Sandbox Python para execução de exercícios
- [x] Validação automática de respostas
- [x] Sistema de dicas (hints) e starter code

### 📊 Progresso do Aluno
- [x] Marcadores de aula concluída
- [x] Cálculo de progresso por módulo e geral
- [x] Streak (dias consecutivos de estudo)
- [x] Tempo total de estudo
- [x] Timeline de atividades
- [x] Sidebar com status (bloqueada, atual, concluída)

### 🏆 Gamificação
- [x] Sistema de conquistas (achievements)
- [x] Catálogo com 6 conquistas
- [x] Desbloqueio automático por condição
- [x] Notificações em tempo real

### 💳 Pagamentos
- [x] Integração com Mercado Pago (Pix + Cartão)
- [x] Webhook para liberação automática
- [x] Controle de acesso por status de pagamento

### 🎨 UI/UX
- [x] Design responsivo (mobile-first)
- [x] Animações com GSAP
- [x] Tema dark
- [x] Componentes customizados (GlowCard, etc)
- [x] Loading states e error handling

---

## 🚀 Como Rodar Localmente

### Pré-requisitos
- **Python 3.11+**
- **Node.js 18+**
- **Git**
- Conta no **MongoDB Atlas** (gratuita)

### 1. Clonar o repositório

git clone https://github.com/FelipeFreitasRossi/devstack.git
cd devstack
2. Backend — FastAPI
cd backend

# Criar e ativar ambiente virtual
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Copiar o arquivo de exemplo e preencher as variáveis
cp .env.example .env

# Rodar o servidor
uvicorn app.main:app --reload --port 8000
Acessar:

API: http://localhost:8000

Swagger: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

3. Frontend — React + Vite

cd frontend

# Instalar dependências
npm install

# Copiar o arquivo de exemplo
cp .env.example .env

# Rodar em modo desenvolvimento
npm run dev
Acessar: http://localhost:5173

4. Build de produção (frontend)

cd frontend
npm run build
# Arquivos prontos em dist/
🔐 Variáveis de Ambiente
Backend (backend/.env)
Variável	Descrição	Exemplo
MONGODB_URI	String de conexão do MongoDB Atlas	mongodb+srv://user:pass@cluster.mongodb.net/...
DB_NAME	Nome do banco de dados	curso_saas
JWT_SECRET	Chave secreta para assinar tokens	string aleatória longa
FRONTEND_URL	URL(s) do frontend autorizadas no CORS	https://inteligenciabrasileira.com
MP_ACCESS_TOKEN	Access token do Mercado Pago	APP_USR-...
MP_PUBLIC_KEY	Public key do Mercado Pago	APP_USR-...
MP_WEBHOOK_SECRET	Secret para validar webhooks do MP	string do painel MP
Gerar JWT_SECRET seguro:

python -c "import secrets; print(secrets.token_urlsafe(64))"
Frontend (frontend/.env)
Variável	Descrição	Exemplo
VITE_API_URL	URL base da API	https://devstack-z0gf.onrender.com
⚠️ Importante: variáveis do Vite precisam do prefixo VITE_ para serem expostas ao código React.

⚠️ Nunca commite arquivos .env. Use os arquivos .env.example como template.

📡 API — Endpoints Principais
Autenticação
Método	Endpoint	Descrição
POST	/api/auth/register	Cadastro de novo usuário
POST	/api/auth/login	Login (retorna JWT)
GET	/api/auth/me	Dados do usuário logado
Lições
Método	Endpoint	Descrição
GET	/lessons/{lesson_id}	Conteúdo de uma aula
GET	/lessons/{lesson_id}/adjacent	Aula anterior e próxima
POST	/lessons/{lesson_id}/complete	Marcar aula como concluída
POST	/lessons/exercise/submit	Enviar solução de exercício
Dashboard
Método	Endpoint	Descrição
GET	/dashboard/modules	Módulos com progresso
GET	/dashboard/next-lesson	Próxima aula recomendada
GET	/dashboard/weekly-activity	Atividade dos últimos 7 dias
GET	/dashboard/achievements	Conquistas do usuário
GET	/dashboard/timeline	Histórico de aulas concluídas
Pagamentos
Método	Endpoint	Descrição
POST	/api/payments/checkout	Criar preferência de pagamento
POST	/api/webhooks/mercadopago	Webhook do MP
Documentação interativa completa: /docs

🚢 Deploy
Backend — Render
Cria um Web Service no Render

Conecta o repositório GitHub

Configurações:

Language: Python 3

Branch: main

Root Directory: backend

Build Command: pip install -r requirements.txt

Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT

Instance Type: Free

Adiciona as Environment Variables (ver seção anterior)

Deploy automático a cada git push na main

Anti-sleep (plano Free): configura um monitor no UptimeRobot para pingar https://seu-servico.onrender.com/health a cada 5 minutos.

Frontend — HostGator
Roda o build: npm run build

Compacta o conteúdo da pasta dist/ em um .zip

No cPanel → Gerenciador de Arquivos → pasta do domínio

Sobe o .zip, extrai, apaga o .zip

Cria o arquivo .htaccess para SPA routing:

apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteBase /
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule . /index.html [L]
</IfModule>
Banco — MongoDB Atlas
Cria conta em cloud.mongodb.com

Cria cluster M0 (gratuito)

Security → Database Access: cria usuário com senha forte

Security → Network Access: libera 0.0.0.0/0 (para permitir IPs dinâmicos do Render)

Copia a connection string e cola em MONGODB_URI no Render

CORS
Configura a variável FRONTEND_URL no Render com o domínio do site em produção:

FRONTEND_URL=https://inteligenciabrasileira.com,https://www.inteligenciabrasileira.com
🏗 Arquitetura
text
   ┌──────────────────┐
   │     Usuário      │
   └────────┬─────────┘
            │ HTTPS
            ▼
   ┌──────────────────────────┐
   │   Frontend (React SPA)   │
   │   HostGator / Vercel     │
   └────────┬─────────────────┘
            │ HTTPS (JSON)
            ▼
   ┌──────────────────────────┐
   │   Backend (FastAPI)      │
   │   Render                 │
   │  ┌─────────────────────┐ │
   │  │ JWT Auth + CORS     │ │
   │  │ Rotas REST /api/*   │ │
   │  │ Sandbox de código   │ │
   │  │ Mercado Pago SDK    │ │
   │  └─────────────────────┘ │
   └────────┬─────────────────┘
            │ Connection String
            ▼
   ┌──────────────────────────┐
   │   MongoDB Atlas (M0)     │
   │   - users                │
   │   - progress             │
   │   - achievements         │
   │   - daily_activity       │
   │   - orders               │
   └──────────────────────────┘
🔒 Segurança
Senhas: hasheadas com bcrypt (nunca em texto puro)

Tokens JWT: assinados com SECRET de 512 bits, expiração de 24h

CORS: origens restritas via variável de ambiente

Validação: schemas Pydantic em todos os endpoints

Variáveis sensíveis: nunca commitadas (.env no .gitignore)

Validação de dados HTML: textContent no frontend (prevenção de XSS)

Antes de ir para produção
□ Repositório privado no GitHub
□ Todas as chaves rotacionadas (nunca commitadas com valor real)
□ .env no .gitignore (backend e frontend)
□ FREE_MODE = False no analytics.py (desbloqueio sequencial por módulo)
□ HTTPS forçado em produção
□ Backup automático do MongoDB (plano pago Atlas)
🗺 Roadmap
☑ Autenticação com JWT
☑ Sistema de progresso e conquistas
☑ Sandbox de exercícios Python
☑ Integração Mercado Pago
□ Aplicativo mobile (React Native)
□ Editor de código com syntax highlighting
□ Modo colaborativo (estudo em grupo)
□ Certificados de conclusão
□ Suporte a múltiplos idiomas
□ Analytics de aprendizado com IA
🤝 Contribuindo
Este é um projeto pessoal de curso, mas sugestões são bem-vindas. Abre uma issue para bugs ou features.

Fork o projeto

Cria uma branch: git checkout -b feature/minha-feature

Commita seguindo Conventional Commits: feat: adiciona X

Push: git push origin feature/minha-feature

Abre um Pull Request

📝 Licença
Projeto privado. Todos os direitos reservados.

O conteúdo das aulas, código-fonte e materiais são de propriedade exclusiva do autor. Uso comercial, redistribuição ou cópia não autorizada não são permitidos.

👨‍💻 Autor
Felipe Freitas Rossi

GitHub: @FelipeFreitasRossi

Projeto: github.com/FelipeFreitasRossi/devstack
