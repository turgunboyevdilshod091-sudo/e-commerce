from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

def tasdiqlash_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Tasdiqlash",callback_data="done")],
            [InlineKeyboardButton(text="Bekor qilih",callback_data="cancel")]
        ]
    )