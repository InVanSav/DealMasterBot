from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from DealMasterApp.Handlers.Common.KeyboardGenerator import create_reply_keyboard
from DealMasterApp.Handlers.Common.Parameters import get_available_cities
from DealMasterApp.Handlers.Common.UserPoll import UserPoll

router = Router()


@router.message(Command("start"))
async def command_start_handler(message: Message, state: FSMContext):
    """ Обработчик команды /start """
    await state.update_data(telegram_name=message.from_user.full_name)
    await state.set_state(UserPoll.city)

    welcome_message = ("Приветствую! Я бот компании <b>DealMaster</b>.\n"
                       "Мы помогаем найти идеальное жилье.\n"
                       "Пожалуйста, ответьте на необходимые вопросы.\n\n"
                       "В каком городе Вы проживаете?")

    button_labels = await get_available_cities()

    await message.answer(
        welcome_message,
        reply_markup=create_reply_keyboard(button_labels),
    )
