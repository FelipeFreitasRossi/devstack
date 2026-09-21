<div align="center">

# Devstack

**Plataforma de curso de programação com acesso vitalício.**
Aprenda Python, APIs e Git escrevendo código de verdade, direto no navegador.

![React](https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-6-3178C6?logo=typescript&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-8-646CFF?logo=vite&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4-06B6D4?logo=tailwindcss&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?logo=mongodb&logoColor=white)
![Mercado Pago](https://img.shields.io/badge/Mercado_Pago-009EE3?logo=mercadopago&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-amber)

</div>

---

## Sobre o projeto

O **Devstack** é um SaaS de ensino de programação. O aluno paga **uma única vez (R$ 19,99)** e tem acesso vitalício ao conteúdo. Cada lição traz teoria, exemplos e exercícios que o aluno resolve em um **editor de código no navegador**, com correção automática.

O projeto é dividido em duas partes:

- **`frontend/`**: aplicação web em React + TypeScript (landing page, cadastro, checkout, área do aluno, lições e perfil).
- **`backend/`**: API em FastAPI com MongoDB, autenticação JWT, pagamentos via Mercado Pago e execução segura do código dos alunos.

## Funcionalidades

### Para o aluno
- **Trilha de estudos** com 6 módulos e 57 lições (cerca de 51 horas de conteúdo):

  | Módulo | Tema | Lições |
  |:-:|---|:-:|
  | 01 | Lógica de Programação | 11 |
  | 02 | Python Fundamentos | 11 |
  | 03 | Python Intermediário | 10 |
  | 04 | Python para Desenvolvimento (HTTP, APIs, autenticação e banco de dados) | 7 |
  | 05 | FastAPI | 8 |
  | 08 | Git e GitHub | 10 |

- **Editor de código no navegador** com exercícios corrigidos automaticamente e dicas quando a resposta está errada.
- **Painel do aluno** com progresso por módulo, próxima lição, atividade semanal, distribuição do tempo de estudo e linha do tempo.
- **Streak de estudo** (dias seguidos) e **meta semanal**.
- **6 conquistas** desbloqueáveis: *Primeiro passo*, *Streak de 3 dias*, *Semana completa*, *Módulo completo*, *Dev dedicado* e *Devstack master*.
- **Busca de lições** e **perfil** com alteração de nome e senha.

### Pagamento
- **Pix** (QR Code e "copia e cola") e **cartão de crédito** com o Mercado Pago.
- **O usuário só é criado no banco depois que o pagamento é confirmado.** Quem desiste do checkout não deixa cadastro salvo (veja [Fluxo de cadastro e pagamento](#fluxo-de-cadastro-e-pagamento)).
- Confirmação do Pix por *polling* na API do Mercado Pago, conferindo que o pedido pertence àquele cadastro.

### Segurança
- Senhas com hash **bcrypt**; nunca ficam em texto puro.
- Autenticação com **JWT**.
- Código dos alunos roda em um **subprocesso isolado**, com tempo limite, limite de saída e bloqueio de módulos e funções perigosas (`os`, `subprocess`, `socket`, `open`, `eval` etc.).

## Tecnologias

| Camada | Tecnologias |
|---|---|
| **Frontend** | React 19, TypeScript, Vite, Tailwind CSS 4, React Router 7, GSAP, Lottie, Lucide Icons, SDK React do Mercado Pago |
| **Backend** | Python, FastAPI, Uvicorn, Pydantic, PyMongo, python-jose (JWT), bcrypt, httpx |
| **Banco de dados** | MongoDB (Atlas ou local) |
| **Pagamentos** | Mercado Pago (Pix e cartão) |

## Estrutura do projeto

```
devstack/
├── backend/
│   ├── app/
│   │   ├── main.py              # Cria o app FastAPI, CORS e rotas
│   │   ├── auth.py              # Hash de senha, JWT e usuário logado
│   │   ├── signup.py            # Cadastro pendente (token assinado, antes do pagamento)
│   │   ├── mercadopago.py       # Integração com a API de pedidos do Mercado Pago
│   │   ├── database.py          # Conexão com o MongoDB e coleções
│   │   ├── analytics.py         # Currículo, progresso, streak e conquistas
│   │   ├── code_runner.py       # Executa o código do aluno em subprocesso
│   │   ├── sandbox_worker.py    # Worker isolado (bloqueios e limites)
│   │   ├── lessons_content/     # Conteúdo das lições, por módulo
│   │   └── routes/              # auth, payments, webhooks, dashboard, lessons, profile
│   └── requirements.txt
└── frontend/
    └── src/
        ├── components/          # ui, layout, sections, student, lesson, profile, auth
        ├── contexts/            # AuthContext e transições entre login/cadastro
        ├── hooks/               # useDashboard, useLesson, useProfile...
        ├── pages/               # Home, Login, Cadastro, Checkout, StudentArea...
        └── services/api.ts      # Cliente da API
```

## Como rodar localmente

### Pré-requisitos
- **Python** 3.10 ou superior
- **Node.js** 20.19 ou superior
- Um banco **MongoDB** (o [MongoDB Atlas](https://www.mongodb.com/atlas) tem plano gratuito)
- Uma conta no **Mercado Pago Developers** para as credenciais

### 1. Clonar o repositório

```bash
git clone https://github.com/FelipeFreitasRossi/devstack.git
cd devstack
```

### 2. Backend

```bash
cd backend

# Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux / macOS

# Instalar as dependências
pip install -r requirements.txt
```

Crie o arquivo `backend/.env` (veja a tabela [abaixo](#variáveis-de-ambiente)) e inicie a API:

```bash
uvicorn app.main:app --reload
```

A API fica em `http://localhost:8000` e a documentação interativa em `http://localhost:8000/docs`.

### 3. Frontend

```bash
cd frontend
npm install
npm run dev
```

O site fica em `http://localhost:5173`.

> O frontend chama a API em `http://localhost:8000/api` (definido em `frontend/src/services/api.ts`) e o backend só aceita requisições vindas de `http://localhost:5173` (CORS em `backend/app/main.py`). Se mudar as portas, ajuste esses dois pontos.

## Variáveis de ambiente

Crie `backend/.env` com:

| Variável | Descrição |
|---|---|
| `MONGODB_URI` | String de conexão do MongoDB |
| `DB_NAME` | Nome do banco (padrão: `curso_saas`) |
| `JWT_SECRET` | Chave secreta usada para assinar os tokens. Use um valor longo e aleatório |
| `JWT_ALGORITHM` | Algoritmo do JWT (padrão: `HS256`) |
| `JWT_EXPIRATION_HOURS` | Validade do login em horas (padrão: `24`) |
| `MP_ACCESS_TOKEN` | *Access Token* do Mercado Pago |
| `FRONTEND_URL` | URL do frontend (ex.: `http://localhost:5173/`) |

Exemplo:

```env
MONGODB_URI=mongodb+srv://USUARIO:SENHA@seu-cluster.mongodb.net/curso_saas
DB_NAME=curso_saas
JWT_SECRET=troque-por-uma-chave-longa-e-aleatoria
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24
MP_ACCESS_TOKEN=TEST-0000000000000000-000000-00000000000000000000000000000000-000000000
FRONTEND_URL=http://localhost:5173/
```

> **Nunca envie o `.env` para o GitHub.** Ele já está no `.gitignore`. Se uma senha ou chave vazar, troque-a imediatamente.

A **chave pública** do Mercado Pago (usada no formulário de cartão) fica em `frontend/src/pages/Checkout.tsx`, na chamada `initMercadoPago(...)`. Troque pela sua.

### Testando pagamentos

- Com credenciais de **teste** (`TEST-...`), o **cartão** funciona normalmente com os [cartões de teste](https://www.mercadopago.com.br/developers/pt/docs/checkout-api/integration-test/test-cards) do Mercado Pago.
- O **Pix** exige credenciais de **produção**.

## Fluxo de cadastro e pagamento

O usuário **não é salvo no banco ao se cadastrar**. Os dados ficam em um token assinado (com a senha já em hash) até o pagamento ser confirmado:

```mermaid
sequenceDiagram
    participant U as Aluno
    participant F as Frontend
    participant B as Backend
    participant MP as Mercado Pago
    participant DB as MongoDB

    U->>F: Preenche nome, e-mail e senha
    F->>B: POST /api/auth/register
    B-->>F: signup_token (nada é salvo no banco)
    U->>F: Escolhe Pix ou cartão
    F->>B: Cria pagamento (com signup_token)
    B->>MP: Cria o pedido
    U->>MP: Paga
    F->>B: Consulta o status do pedido
    B->>MP: O pedido foi pago?
    MP-->>B: Confirmado
    B->>DB: Cria o usuário (uma única vez)
    B-->>F: Login automático
    F-->>U: Acesso à área do aluno
```

Se o aluno abandonar, cancelar, falhar ou deixar o pagamento expirar, **nenhum usuário é criado**. Enquanto está no pagamento, o aluno pode voltar ao cadastro pela seta **← Voltar**, sem perder o que preencheu.

## Principais endpoints da API

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/api/auth/register` | Valida o cadastro e devolve o `signup_token` (não grava no banco) |
| `POST` | `/api/auth/login` | Login |
| `POST` | `/api/payments/create` | Gera pagamento Pix |
| `POST` | `/api/payments/create-card` | Paga com cartão |
| `GET` | `/api/payments/status/{order_id}` | Consulta a confirmação do pagamento |
| `POST` | `/api/webhooks/mercadopago` | Recebe notificações do Mercado Pago (hoje só registra em log) |
| `GET` | `/api/dashboard/overview` | Resumo do painel do aluno |
| `GET` | `/api/dashboard/modules` | Módulos e progresso |
| `GET` | `/api/dashboard/achievements` | Conquistas |
| `GET` | `/api/dashboard/weekly-activity` | Atividade da semana |
| `POST` | `/api/dashboard/progress` | Registra progresso de estudo |
| `GET` | `/api/lessons/search-index` | Índice para a busca de lições |
| `GET` | `/api/lessons/{lesson_id}` | Conteúdo de uma lição |
| `POST` | `/api/lessons/{lesson_id}/submit` | Envia o código de um exercício para correção |
| `GET` `PUT` | `/api/profile` | Ver e alterar o perfil |
| `PUT` | `/api/profile/password` | Alterar a senha |

A lista completa está em `http://localhost:8000/docs`.

## Próximos passos

- [ ] Webhook do Mercado Pago para confirmar pagamentos mesmo com a aba fechada
- [ ] Publicar os módulos 06 e 07, que já têm conteúdo escrito mas ainda não estão no currículo
- [ ] Índice único no e-mail da coleção de usuários
- [ ] Deploy (frontend e backend)

## Contato

**Felipe Freitas Rossi**

[![GitHub](https://img.shields.io/badge/GitHub-FelipeFreitasRossi-181717?logo=github&logoColor=white)](https://github.com/FelipeFreitasRossi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-felipefreitasrossi-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/felipefreitasrossi/)
[![Instagram](https://img.shields.io/badge/Instagram-codebyfelipe-E4405F?logo=instagram&logoColor=white)](https://www.instagram.com/codebyfelipe)
[![Discord](https://img.shields.io/badge/Discord-Comunidade-5865F2?logo=discord&logoColor=white)](https://discord.gg/pTAVzG6DU3)

## Licença

Distribuído sob a licença **MIT**. Veja o arquivo [`LICENSE`](LICENSE) para mais detalhes.
