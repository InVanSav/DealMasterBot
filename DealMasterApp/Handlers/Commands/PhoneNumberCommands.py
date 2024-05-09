import phonenumbers
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from DealMasterApp.Handlers.Common.Parameters import available_prices
from DealMasterApp.Handlers.Common.UserPoll import UserPoll

router = Router()


@router.message(UserPoll.price, F.text.in_(available_prices))
async def phone_number_handler(message: Message, state: FSMContext):
    """ Обработчик номера телефона """
    await state.update_data(price=message.text)
    await state.set_state(UserPoll.phone_number)

    await message.answer("Ваш номер телефона? Он нужен нам для связи с Вами.",
                         reply_markup=ReplyKeyboardRemove())


def validate_phone_number(phone_number: str) -> bool:
    """
    Валидирует указанный номер телефона.

    Args:
        phone_number (str): Номер телефона.
    """
    try:
        phone_number = phonenumbers.parse(phone_number, "RU")

        if not phonenumbers.is_valid_number(phone_number):
            return False

        if not phonenumbers.is_possible_number(phone_number):
            return False

        return True
    except phonenumbers.NumberParseException:
        return False
