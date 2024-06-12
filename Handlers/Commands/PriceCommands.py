from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from Handlers.Common.KeyboardGenerator import create_reply_keyboard
from Handlers.Common.Parameters import get_invalid_parameter_str, available_prices, available_areas
from Handlers.Common.UserPoll import UserPoll

router = Router()


@router.message(UserPoll.area, F.text.in_(available_areas))
async def price_handler(message: Message, state: FSMContext):
    """ Обработчик цены """
    await state.update_data(area=message.text)
    await state.set_state(UserPoll.price)

    button_labels = available_prices

    await message.answer(
        "Какую желаемую цену Вы имеете в виду?",
        reply_markup=create_reply_keyboard(button_labels),
    )


@router.message(UserPoll.price, F.text.not_in(available_prices))
async def invalid_price_handler(message: Message):
    """ Обработчик некорректной цены """
    await message.answer(get_invalid_parameter_str("Некорректная цена"))
