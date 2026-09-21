from typing import Optional
from fastapi import APIRouter, Depends, Header, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from datetime import datetime
from app.auth import get_current_user, create_access_token
from app.database import users_collection, orders_collection
from app.mercadopago import create_payment_order, create_card_order, get_order
from app.signup import (
    read_signup_token,
    signup_payer,
    ensure_email_available,
    create_user_from_signup,
)

router = APIRouter()

# Igual ao HTTPBearer do login, mas sem erro automático: quem está se cadastrando
# ainda não tem login e usa o signup_token no lugar.
optional_bearer = HTTPBearer(auto_error=False)


class PaymentRequest(BaseModel):
    method: str
    signup_token: Optional[str] = None  # cadastro novo, ainda não salvo no banco


class CardPaymentRequest(BaseModel):
    token: str
    payment_method_id: str
    installments: int
    signup_token: Optional[str] = None  # cadastro novo, ainda não salvo no banco


def _authenticated_user(credentials: Optional[HTTPAuthorizationCredentials]):
    """Fluxo antigo: usuário que já existe e está logado."""
    if credentials is None:
        raise HTTPException(status_code=403, detail="Not authenticated")
    return get_current_user(credentials)


def _signup_response(user: dict) -> dict:
    """Login automático do usuário recém-criado (depois do pagamento)."""
    return {
        "access_token": create_access_token({"sub": user["email"]}),
        "user": {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "paid": True,
        },
    }


def _save_approved_order(user: dict, order_id: str, method: str) -> None:
    """Registra o pedido aprovado (sem duplicar se for chamado de novo)."""
    now = datetime.utcnow()
    orders_collection.update_one(
        {"order_id": order_id},
        {
            "$set": {
                "user_id": user["_id"],
                "amount": 19.99,
                "method": method,
                "status": "approved",
                "paid_at": now,
            },
            "$setOnInsert": {"created_at": now},
        },
        upsert=True,
    )


def _extract_error_detail(result: dict) -> str:
    """Extrai mensagem de erro amigável da resposta do Mercado Pago."""
    data = result.get("data", {})
    
    # Erro interno do MP (sandbox)
    if data.get("status_detail") == "processing_error":
        return (
            "Este método de pagamento não está disponível no ambiente de teste. "
            "Para testar Pix e Boleto, use as credenciais de produção. "
            "O cartão funciona normalmente em testes."
        )
    
    # Erros estruturados da API
    errors = data.get("errors", [])
    if errors and isinstance(errors, list):
        messages = [e.get("message", "") for e in errors]
        return " | ".join(messages)
    
    # Erro genérico
    return data.get("message") or data.get("error") or "Erro ao processar pagamento"


@router.post("/create")
async def create_payment(
    data: PaymentRequest,
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(optional_bearer),
):
    if data.signup_token:
        signup = read_signup_token(data.signup_token)
        ensure_email_available(signup)
        user = None
        payer = signup_payer(signup)
    else:
        user = _authenticated_user(credentials)
        payer = user
        if user.get("paid"):
            raise HTTPException(status_code=400, detail="Pagamento já realizado")

    if data.method not in ["pix", "boleto"]:
        raise HTTPException(status_code=400, detail="Método inválido")

    result = await create_payment_order(payer, data.method)

    if result["status_code"] not in (200, 201):
        raise HTTPException(
            status_code=result["status_code"],
            detail=_extract_error_detail(result),
        )

    order = result["data"]
    order_id = order.get("id")
    payment = order.get("transactions", {}).get("payments", [{}])[0]
    payment_method = payment.get("payment_method", {})

    # Cadastro novo (user is None): nada é salvo antes do pagamento ser confirmado
    if user is not None:
        users_collection.update_one(
            {"_id": user["_id"]},
            {"$set": {"pending_order_id": order_id}},
        )

        orders_collection.insert_one({
            "user_id": user["_id"],
            "order_id": order_id,
            "amount": 19.99,
            "method": data.method,
            "status": "pending",
            "created_at": datetime.utcnow(),
        })

    response = {"order_id": order_id, "method": data.method}

    if data.method == "pix":
        response.update({
            "qr_code": payment_method.get("qr_code"),
            "qr_code_base64": payment_method.get("qr_code_base64"),
            "ticket_url": payment_method.get("ticket_url"),
        })
    elif data.method == "boleto":
        response.update({
            "ticket_url": payment_method.get("ticket_url"),
            "barcode": payment_method.get("barcode"),
        })

    return response


@router.post("/create-card")
async def create_card_payment(
    data: CardPaymentRequest,
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(optional_bearer),
):
    if data.signup_token:
        signup = read_signup_token(data.signup_token)
        ensure_email_available(signup)
        user = None
        payer = signup_payer(signup)
    else:
        user = _authenticated_user(credentials)
        payer = user
        if user.get("paid"):
            raise HTTPException(status_code=400, detail="Pagamento já realizado")

    result = await create_card_order(
        payer, data.token, data.payment_method_id, data.installments
    )

    if result["status_code"] not in (200, 201):
        raise HTTPException(
            status_code=result["status_code"],
            detail=_extract_error_detail(result),
        )

    order = result["data"]
    status = order.get("status")
    is_paid = status in ("processed", "approved")

    if is_paid and user is None:
        # Cadastro novo: pagamento aprovado, agora sim cria o usuário
        new_user = create_user_from_signup(signup)
        _save_approved_order(new_user, order.get("id"), "credit_card")
        return {
            "order_id": order.get("id"),
            "status": status,
            "paid": True,
            **_signup_response(new_user),
        }

    if is_paid:
        users_collection.update_one(
            {"_id": user["_id"]},
            {"$set": {"paid": True, "paid_at": datetime.utcnow()}},
        )
        orders_collection.insert_one({
            "user_id": user["_id"],
            "order_id": order.get("id"),
            "amount": 19.99,
            "method": "credit_card",
            "status": "approved",
            "created_at": datetime.utcnow(),
        })

    return {
        "order_id": order.get("id"),
        "status": status,
        "paid": is_paid,
    }


@router.get("/status/{order_id}")
async def check_status(
    order_id: str,
    credentials: Optional[HTTPAuthorizationCredentials] = Depends(optional_bearer),
    x_signup_token: Optional[str] = Header(default=None),
):
    signup = read_signup_token(x_signup_token) if x_signup_token else None
    user = None if signup else _authenticated_user(credentials)

    result = await get_order(order_id)

    if result["status_code"] != 200:
        raise HTTPException(status_code=400, detail="Order não encontrada")

    order = result["data"]
    status_value = order.get("status", "pending")
    is_paid = status_value in ("processed", "approved")

    if signup:
        # Só vale se a order foi criada para ESTE cadastro
        if is_paid and order.get("external_reference") == signup["sid"]:
            new_user = create_user_from_signup(signup)
            _save_approved_order(new_user, order_id, "pix")
            return {"status": status_value, "paid": True, **_signup_response(new_user)}
        return {"status": status_value, "paid": False}

    if is_paid and not user.get("paid"):
        users_collection.update_one(
            {"_id": user["_id"]},
            {"$set": {"paid": True, "paid_at": datetime.utcnow()}},
        )
        orders_collection.update_one(
            {"order_id": order_id},
            {"$set": {"status": "approved", "paid_at": datetime.utcnow()}},
        )

    return {"status": status_value, "paid": is_paid}