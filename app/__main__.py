import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage

from app.config import Config
from app.routes import include_routers
from app.services.counter import Counter


def main():
    event_loop = asyncio.get_event_loop()

    config = Config(_env_file=".env", _env_file_encoding="utf-8")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    fsm_storage = MemoryStorage()

    bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
    dispatcher = Dispatcher(storage=fsm_storage)

    counter = Counter()

    include_routers(dispatcher, counter=counter)

    dispatcher.run_polling(bot)


if __name__ == '__main__':
    main()
