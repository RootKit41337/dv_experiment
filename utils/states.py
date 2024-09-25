from aiogram.fsm.state import StatesGroup, State

class From(StatesGroup):
    name = State()
    age = State()
    sex = State()
    about = State()
    photo = State()