import logging
from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message


class LoggingMiddleware(BaseMiddleware[Message]):
    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ):
        logging.info("LOGGGGGG!")

        counter = data.get("counter")
        if counter:
            logging.info(counter)

        return await handler(event, data)
