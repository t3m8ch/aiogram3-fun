from aiogram import Router

from app.middlewares.counter_middleware import CounterMiddleware
from app.middlewares.logging_middleware import LoggingMiddleware
from app.services.counter import Counter


def include_middlewares(router: Router, *, counter: Counter):
    router.message.middleware(CounterMiddleware(counter))
    router.message.middleware(LoggingMiddleware())
