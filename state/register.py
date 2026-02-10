from aiogram.fsm.state import StatesGroup, State

class Registerstate(StatesGroup):
    name=State()
    surename=State()
    age=State()
    phone=State()