from aiogram import F,Router,Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message,CallbackQuery
from state.register import Registerstate
from keyboards.inline import tasdiqlash_button
from config import config

router=Router()
ADMIN_ID=config.ADMIN_ID
bot=Bot(token=config.BOT_TOKEN)

@router.message(F.text=='Register')
async def register(msg:Message,state:FSMContext):
    await msg.answer("Ro`yxatdan o`tish uchun iltimos ismingizni kiriting")
    await state.set_state(Registerstate.name)

@router.message(Registerstate.name)
async def register(msg:Message,state:FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer("Familyangizni kiriting")
    await state.set_state(Registerstate.surename)

@router.message(Registerstate.surename)
async def register(msg:Message,state:FSMContext):
    await state.update_data(surename=msg.text)
    await msg.answer("Yoshingizni kiriting")
    await state.set_state(Registerstate.age)

@router.message(Registerstate.age)
async def register(msg:Message,state:FSMContext):
    await state.update_data(age=msg.text)
    await msg.answer("telefon raqam kiriting")
    await state.set_state(Registerstate.phone)

@router.message(Registerstate.phone)
async def register(msg:Message,state:FSMContext):
    await state.update_data(phone=msg.text)
    data=await state.get_data()
    await msg.answer(f"""Ma'lumotlaringiz to'grimi?
Ismingiz: {data['name']}
Familyangiz: {data["surename"]}
Yoshingiz: {data['age']}
Telefon raqamingiz: {data["phone"]}
""",reply_markup=tasdiqlash_button())
    await state.set_state(Registerstate.confirm)

@router.callback_query(Registerstate.confirm,F.data)
async def confirm_handler(call:CallbackQuery,state:FSMContext):
    if call.data=="done":
            data=await state.get_data()
            await bot.send_message(chat_id=ADMIN_ID,text=f"""Yangi foydalanuvchi ro'yxatdan o'tdi
Ism: {data['name']}
Familya: {data["surename"]}
Yosh: {data['age']}
Telefon raqam: {data["phone"]}
""")
            await call.message.answer("Muvaffaqiyatli ro'yxatdan o'tdingiz")
            await state.clear()
            await call.answer()
    elif call.data=='cancel':
         await call.message.answer("Qaytadan ro'yxatdan o'tish boshlandi\nIltimos ismingizni kiriting")
         await state.set_state(Registerstate.name)
         await call.answer()