from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from DealMasterApp.Handlers.Common.KeyboardGenerator import create_reply_keyboard
from DealMasterApp.Handlers.Common.Parameters import available_cities
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

    button_labels = available_cities

    await message.answer(
        welcome_message,
        reply_markup=create_reply_keyboard(button_labels),
    )


# @router.message(Command("help"))
# async def command_help_handler(message: Message):
#     """ Обработчик команды /help """
#     help_message = (
#         "Мечтаете о новой квартире?\n\n"
#         "Наш бот поможет Вам быстро и легко найти идеальное жилье в новостройке!\n\n"
#         "<b>Как это работает?</b>\n\n"
#         "1. Расскажите боту о своих желаниях:\n"
#         "- В каком городе Вы живете?\n"
#         "- В каком районе Вы хотите купить квартиру?\n"
#         "- Какую площадь Вы ищете?\n"
#         "- Какую цену Вы готовы платить?\n"
#         "2. Оставьте свои данные, чтобы наш менеджер связался с Вами в кратчайшие сроки.\n\n"
#         "3. Специалист подберет для Вас несколько вариантов квартир, ответит на все Ваши вопросы и проведет "
#         "сделку.\n\n"
#         "<b>Доступные команды:</b>\n\n"
#         "/start - Начать опрос для поиска недвижимости\n"
#         "/help - Что происходит, помогите\n"
#         "/cancel - Отменить действие"
#     )
#     await message.answer(help_message)
#
#
# @router.message(Command("cancel"))
# async def cancel_handler(message: Message, state: FSMContext) -> None:
#     """ Позволяет пользователю отменить любое действие """
#     current_state = await state.get_state()
#     if current_state is None:
#         return
#
#     logging.info("Cancelling state %r", current_state)
#
#     await state.clear()
#
#     await message.answer(
#         "Вы отменили действие.",
#         reply_markup=ReplyKeyboardRemove(),
#     )
