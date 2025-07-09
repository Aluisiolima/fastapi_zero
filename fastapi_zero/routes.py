from fastapi import routing
from fastapi_zero.user.controller import router as user_router
from fastapi_zero.produto.controller import router as produto_router
from fastapi_zero.pedido.controller import router as pedido_router
from fastapi_zero.cart.controller import router as cart_router

router = routing.APIRouter()

router.include_router(user_router, prefix="/user", tags=["users"])
router.include_router(produto_router, prefix="/produto", tags=["produtos"])
router.include_router(pedido_router, prefix="/pedido", tags=["pedidos"])
router.include_router(cart_router, prefix="/cart", tags=["carts"])