import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import auth, payments, webhooks, dashboard, profile
from app.routes import lessons as lessons_routes

app = FastAPI(title="Devstack API", version="0.1.0")

# ============================================================================
# CORS — lê as origens permitidas da variável de ambiente FRONTEND_URL
# ============================================================================
# Aceita múltiplas origens separadas por vírgula, por exemplo:
#   FRONTEND_URL=http://localhost:5173,https://inteligenciabrasileira.com
#
# Se a variável não estiver definida, cai no fallback de desenvolvimento local.
# ============================================================================
_origens_raw = os.getenv("FRONTEND_URL", "http://localhost:5173")
origins = [origem.strip() for origem in _origens_raw.split(",") if origem.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# ROTAS
# ============================================================================
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(payments.router, prefix="/api/payments", tags=["payments"])
app.include_router(webhooks.router, prefix="/api/webhooks", tags=["webhooks"])
app.include_router(dashboard.router)
app.include_router(profile.router)
app.include_router(lessons_routes.router)


@app.get("/")
async def root():
    return {"message": "Devstack API rodando"}


# ============================================================================
# HEALTH CHECK — usado pelo UptimeRobot para manter o backend acordado
# ============================================================================
# O UptimeRobot (plano gratuito) usa o método HEAD por padrão. Se só existir
# a rota GET, o monitor marca o serviço como "Down" com falso positivo.
# Aqui declaramos as duas rotas: GET devolve o JSON, HEAD só confirma que está
# de pé (sem corpo de resposta).
# ============================================================================
@app.get("/health")
async def health():
    return {"status": "ok"}


@app.head("/health")
async def health_head():
    # Método HEAD: mesmo status 200 da rota GET, mas sem body.
    # O FastAPI responde com 200 e headers automaticamente.
    return