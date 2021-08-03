from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from app.services.counter import Counter


class CounterMiddleware(BaseMiddleware[Message]):
    def __init__(self, counter: Counter):
        self._counter = counter

    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ):
        self._counter.increment()
        data["counter"] = self._counter.value
        return await handler(event, data)
