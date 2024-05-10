import uuid
from typing import Dict

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from DIContainer import user_repository, answer_repository
from Domain.Answer import Answer
from Domain.User import User
from Handlers.Commands.PhoneNumberCommands import validate_phone_number
from Handlers.Common.UserPoll import UserPoll

router = Router()


@router.message(UserPoll.phone_number)
async def end_polling_handler(message: Message, state: FSMContext):
    """ Обработчик окончания опроса """
    if not validate_phone_number(message.text):
        await message.answer("Некорректный номер телефона. Попробуйте ещё раз.")
        return

    await state.update_data(phone_number=message.text)

    await message.answer(f"Отлично! Спасибо большое за информацию, <b>{message.from_user.full_name}</b>!\n" +
                         "Я сохраню ваши данные и мы подберем для Вас подходящие варианты жилья.\n\n" +
                         "Наш менеджер свяжется с Вами в ближайшее время.")

    data = await state.get_data()
    await _insert_info_to_db(data)

    await state.clear()


async def _insert_info_to_db(data: Dict):
    user = User(
        uuid.uuid4(),
        data["telegram_name"],
        data["phone_number"],
        True)

    answer = Answer(
        uuid.uuid4(),
        user.user_id,
        data["city"],
        data["district"],
        data["area"],
        data["price"])

    await user_repository.create_user_async(user)
    await answer_repository.create_answer_async(answer)
