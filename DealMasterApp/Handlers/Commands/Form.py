from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    telegram_name = State()
    phone_number = State()

    city = State()
    district = State()
    area = State()
    price = State()