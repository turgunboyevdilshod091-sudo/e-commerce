from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.reply import start_reply
from databases.database import Database

db=Database()

router=Router()

@router.message(CommandStart())
async def start_handler(msg:Message):
    user_id=msg.from_user.id
    user=db.check_user(user_id)
    if not user:
        await msg.answer(f"Assalomu aleykum {msg.from_user.full_name} botga xush kelibsiz",reply_markup=start_reply())
    else:
        await msg.answer(f"Assalomu Alaykum {msg.from_user.full_name}, Siz botga allaqachon ro'yxatdan o'tgansiz")