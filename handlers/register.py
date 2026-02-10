from aiogram import F,Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message,CallbackQuery
from state.register import Registerstate
from keyboards.inline import tasdiqlash_button

router=Router()

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
    await msg.answer(f'Ismingiz: {data['name']}\nFamilyangiz: {data["surename"]}\nYoshingiz: {data['age']}\nTelefon raqamingiz: {data["phone"]}',reply_markup=tasdiqlash_button())

@router.callback_query(F.data=="tasdiqlash")
async def tasdiqlash(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Ma`lumotlaringiz saqlandi")
    await state.clear()
    await call.answer()
