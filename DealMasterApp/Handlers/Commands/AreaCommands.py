from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from DealMasterApp.Handlers.Common.KeyboardGenerator import create_reply_keyboard
from DealMasterApp.Handlers.Common.Parameters import available_districts, get_invalid_parameter_str, available_areas
from DealMasterApp.Handlers.Common.UserPoll import UserPoll

router = Router()


@router.message(UserPoll.district, F.text.in_(available_districts))
async def area_handler(message: Message, state: FSMContext):
    """ Обработчик площади """
    await state.update_data(district=message.text)
    await state.set_state(UserPoll.area)

    button_labels = available_areas

    await message.answer(
        "Какую площадь Вы ищете?",
        reply_markup=create_reply_keyboard(button_labels),
    )


@router.message(UserPoll.area, F.text.not_in(available_areas))
async def invalid_area_handler(message: Message):
    """ Обработчик некорректной площади """
    await message.answer(get_invalid_parameter_str("Некорректная площадь"))
