from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from DealMasterApp.Handlers.Common.KeyboardGenerator import create_reply_keyboard
from DealMasterApp.Handlers.Common.Parameters import available_cities, get_invalid_parameter_str, available_districts, \
    get_volgograd_districts, get_saint_petersburg_districts
from DealMasterApp.Handlers.Common.UserPoll import UserPoll

router = Router()


@router.message(UserPoll.city, F.text == available_cities[0])
async def disctricts_volgograd_handler(message: Message, state: FSMContext):
    """ Обработчик районов города Волгоград """
    await state.update_data(city=message.text)
    await state.set_state(UserPoll.district)

    button_labels = await get_volgograd_districts()

    await message.answer(
        "В каком районе Вы хотите купить жилье?",
        reply_markup=create_reply_keyboard(button_labels),
    )


@router.message(UserPoll.city, F.text == available_cities[1])
async def districts_saint_petersburg_handler(message: Message, state: FSMContext):
    """ Обработчик районов города Санкт-Петербург """
    await state.update_data(city=message.text)
    await state.set_state(UserPoll.district)

    button_labels = await get_saint_petersburg_districts()

    await message.answer(
        "В каком районе Вы хотите купить жилье?",
        reply_markup=create_reply_keyboard(button_labels)
    )


@router.message(UserPoll.district, F.text.not_in(available_districts))
async def invalid_district_handler(message: Message):
    """ Обработчик некорректного района """
    await message.answer(get_invalid_parameter_str("Некорректный район"))


@router.message(UserPoll.city, F.not_in(available_cities))
async def invalid_city_handler(message: Message):
    """ Обработчик некорректного города """
    await message.answer(get_invalid_parameter_str("Некорректный город"))
