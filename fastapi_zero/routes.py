from fastapi import routing
from fastapi_zero.user.controller import router as user_router
from fastapi_zero.produto.controller import router as produto_router
from fastapi_zero.pedido.controller import router as pedido_router
from fastapi_zero.cart.controller import router as cart_router
from fastapi_zero.auth.controller import router as auth_router
from fastapi_zero.categoria.controller import router as categoria_router

router = routing.APIRouter()

router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(produto_router, prefix="/products", tags=["produtos"])
router.include_router(pedido_router, prefix="/orders", tags=["pedidos"])
router.include_router(cart_router, prefix="/cart", tags=["carts"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])
router.include_router(categoria_router, prefix="/categories", tags=["categorias"])