from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_menu_inline_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Кнопка 1",
                callback_data="btn1"
            ),
            InlineKeyboardButton(
                text="Кнопка 2",
                callback_data="btn2"
            ),
        ],
        [
            InlineKeyboardButton(
                text="<< Назад",
                callback_data="back"
            ),
            InlineKeyboardButton(
                text="Кнопка 3",
                callback_data="btn3"
            ),
            InlineKeyboardButton(
                text="Вперёд >>",
                callback_data="next"
            ),
        ]
    ])
