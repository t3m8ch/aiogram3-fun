from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from app.keyboards.menu_keyboard import create_menu_inline_keyboard

menu_router = Router()


@menu_router.message(commands="menu")
async def on_menu_command(message: Message):
    await message.answer(
        text="Меню",
        reply_markup=create_menu_inline_keyboard()
    )


@menu_router.callback_query(F.data.startswith("btn"))
async def on_click_btn(call: CallbackQuery):
    await call.answer(call.data[3:])


# @menu_router.callback_query(F.data.in_("back", "next"))  # TODO: WTF?
# async def on_click_navigation_button(call: CallbackQuery):
#     await call.answer(call.data, show_alert=True)

# @menu_router.callback_query(F.data @ {"back", "next"})  # TODO: WTF?
# async def on_click_navigation_button(call: CallbackQuery):
#     await call.answer(call.data, show_alert=True)

@menu_router.callback_query(F.data.in_({"back", "next"}))
async def on_click_navigation_button(call: CallbackQuery):
    await call.answer(call.data, show_alert=True)
