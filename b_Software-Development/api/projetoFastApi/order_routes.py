from fastapi import APIRouter

order_router = APIRouter(prefix= "/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    """
    essa e a rota padrao de pedidos do nosso sistema
    """
    return {"mensagem": "Voce acesou a rota de pedidos"}