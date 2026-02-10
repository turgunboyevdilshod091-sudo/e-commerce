from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

def tasdiqlash_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Tasdiqlash",callback_data="tasdiqlash")],
            [InlineKeyboardButton(text="O'zgartirish",callback_data="ozgartirish")]
        ]
    )