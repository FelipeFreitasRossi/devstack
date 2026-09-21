"""
Cadastro pendente (antes do pagamento).

Enquanto o usuário paga, nome, e-mail e senha (já em hash bcrypt) ficam dentro
de um token assinado com o mesmo JWT_SECRET do login. Nada é salvo no banco.
O usuário só é criado em `create_user_from_signup`, depois que o pagamento
for confirmado.
"""
import os
import uuid
from datetime import datetime, timedelta

from fastapi import HTTPException
from jose import JWTError, jwt

from app.database import users_collection

# Um pouco mais que a validade do Pix (1h)
SIGNUP_TOKEN_HOURS = 2


def create_signup_token(name: str, email: str, password_hash: str) -> str:
    payload = {
        "type": "signup",  # impede usar este token como token de login (e vice-versa)
        "sid": str(uuid.uuid4()),  # identifica este cadastro no Mercado Pago
        "name": name,
        "email": email,
        "password_hash": password_hash,
        "exp": datetime.utcnow() + timedelta(hours=SIGNUP_TOKEN_HOURS),
    }
    return jwt.encode(
        payload,
        os.getenv("JWT_SECRET"),
        algorithm=os.getenv("JWT_ALGORITHM", "HS256"),
    )


def read_signup_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            os.getenv("JWT_SECRET"),
            algorithms=[os.getenv("JWT_ALGORITHM", "HS256")],
        )
    except JWTError:
        # 400 (e não 401) para o front não mandar o usuário para o /login
        raise HTTPException(
            status_code=400,
            detail="Cadastro expirado. Volte e preencha seus dados novamente.",
        )
    if payload.get("type") != "signup":
        raise HTTPException(status_code=400, detail="Cadastro inválido")
    return payload


def signup_payer(signup: dict) -> dict:
    """Formato que o mercadopago.py já espera (usa _id, email e name)."""
    return {"_id": signup["sid"], "email": signup["email"], "name": signup["name"]}


def ensure_email_available(signup: dict) -> None:
    if users_collection.find_one({"email": signup["email"]}):
        raise HTTPException(status_code=400, detail="Email já cadastrado")


def create_user_from_signup(signup: dict) -> dict:
    """
    Cria o usuário definitivo. Só deve ser chamada com o pagamento confirmado.
    Pode ser chamada mais de uma vez para o mesmo cadastro: só cria na primeira.
    """
    existing = users_collection.find_one({"email": signup["email"]})
    if existing:
        if existing.get("password_hash") == signup["password_hash"]:
            return existing  # este mesmo cadastro já foi criado
        raise HTTPException(
            status_code=409,
            detail=(
                "Este e-mail foi cadastrado por outra conta enquanto o pagamento "
                "era feito. Entre em contato com o suporte."
            ),
        )

    now = datetime.utcnow()
    user = {
        "name": signup["name"],
        "email": signup["email"],
        "password_hash": signup["password_hash"],
        "paid": True,
        "paid_at": now,
        "created_at": now,
    }
    users_collection.insert_one(user)  # o pymongo coloca o _id dentro de `user`
    return user
