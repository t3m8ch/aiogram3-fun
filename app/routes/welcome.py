from aiogram import Router
from aiogram.dispatcher.filters.command import CommandStart
from aiogram.types import Message

welcome_router = Router()


@welcome_router.message(CommandStart())
async def on_start_command(message: Message, counter: int):
    await message.answer(str(counter))


@welcome_router.message(commands="help")
async def on_help_command(message: Message):
    await message.answer("Помощь")
