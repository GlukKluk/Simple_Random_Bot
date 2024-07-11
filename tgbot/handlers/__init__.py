from .admin_handlers import router as admin_handler_router
from .user_handlers import router as user_handler_router
from .other_handlers import router as other_handler_router

routers_list = [
    admin_handler_router,
    user_handler_router,
    other_handler_router
]

__all__ = [
    "routers_list",
]
