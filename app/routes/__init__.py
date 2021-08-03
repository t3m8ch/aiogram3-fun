from aiogram import Dispatcher, Router

from .menu import menu_router
from .welcome import welcome_router
from ..middlewares import include_middlewares
from ..services.counter import Counter


def include_routers(dispatcher: Dispatcher, *, counter: Counter):
    master_router = Router()

    include_middlewares(master_router, counter=counter)

    master_router.include_router(menu_router)
    master_router.include_router(welcome_router)

    dispatcher.include_router(master_router)
