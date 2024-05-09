import asyncio
import logging
import os
import sys
import uuid
from typing import Dict

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove, Message, KeyboardButton, ReplyKeyboardMarkup

from DealMasterApp.ConfigParser import ConfigParser
from DealMasterApp.Database.PgsqlConnection import PgsqlConnection
from DealMasterApp.Database.PgsqlHandler import PgsqlHandler
from DealMasterApp.Database.Repositories.AnswerRepository import AnswerRepository
from DealMasterApp.Database.Repositories.UserRepository import UserRepository
from DealMasterApp.Domain.Answer import Answer
from DealMasterApp.Domain.User import User
from DealMasterApp.Handlers.Commands.Form import Form
from DealMasterApp.TelegramBot import TelegramBot

project_absolute_path = os.path.dirname(__file__)

config_path = os.path.join(project_absolute_path, 'config.ini')

user_scripts_path = os.path.join(project_absolute_path, 'Database/Scripts/User')
answer_scripts_path = os.path.join(project_absolute_path, 'Database/Scripts/Answer')

config_parser = ConfigParser(config_path)
connection_data = PgsqlConnection(config_parser)
db_handler = PgsqlHandler(connection_data)

user_repository = UserRepository(db_handler, user_scripts_path)
answer_repository = AnswerRepository(db_handler, answer_scripts_path)

TOKEN = config_parser.get_value("Bot", "Token")

router = Router()


# Обработка комманд
@router.message(Command("start"))
async def command_start_handler(message: Message, state: FSMContext):
    """
    Обработчик команды /start
    """
    await state.update_data(telegram_name=message.from_user.full_name)
    await state.set_state(Form.city)

    welcome_message = ("Приветствую! Я бот компании <b>DealMaster</b>.\n"
                       "Мы помогаем найти идеальное жилье.\n"
                       "Пожалуйста, ответьте на необходимые вопросы.\n\n"
                       "В каком городе Вы проживаете?")

    await message.answer(
        welcome_message,
        reply_markup=ReplyKeyboardMarkup(
            resize_keyboard=True,
            selective=True,
            keyboard=[
                [KeyboardButton(text="Волгоград")],
                [KeyboardButton(text="Санкт-Петербург")],
            ]
        )
    )


@router.message(Form.city, F.text == "Волгоград")
async def city_volgograd_handler(message: Message, state: FSMContext):
    """
    Обработчик города Волгоград
    """
    await state.update_data(city=message.text)
    await state.set_state(Form.district)

    await message.answer(
        "В каком районе Вы хотите купить жилье?",
        reply_markup=ReplyKeyboardMarkup(
            resize_keyboard=True,
            selective=True,
            keyboard=[
                [KeyboardButton(text="Район 1")],
                [KeyboardButton(text="Район 2")],
                [KeyboardButton(text="Район 3")],
            ],
        )
    )


@router.message(Form.city, F.text == "Санкт-Петербург")
async def city_saint_petersburg_handler(message: Message, state: FSMContext):
    """
    Обработчик города Санкт-Петербург
    """
    await state.update_data(city=message.text)
    await state.set_state(Form.district)

    await message.answer(
        "В каком районе Вы хотите купить жилье?",
        reply_markup=ReplyKeyboardMarkup(
            resize_keyboard=True,
            selective=True,
            keyboard=[
                [KeyboardButton(text="Район 1")],
                [KeyboardButton(text="Район 2")],
                [KeyboardButton(text="Район 3")],
            ],
        )
    )


@router.message(Form.district)
async def district_handler(message: Message, state: FSMContext):
    """
    Обработчик района
    """
    await state.update_data(district=message.text)
    await state.set_state(Form.area)

    await message.answer(
        "Какую площадь Вы ищете?",
        reply_markup=ReplyKeyboardMarkup(
            resize_keyboard=True,
            selective=True,
            keyboard=[
                [KeyboardButton(text="До 50 м²")],
                [KeyboardButton(text="50-100 м²")],
                [KeyboardButton(text="100+ м²")],
            ]
        )
    )


@router.message(Form.area)
async def area_handler(message: Message, state: FSMContext):
    """
    Обработчик площади
    """
    await state.update_data(area=message.text)
    await state.set_state(Form.price)

    await message.answer(
        "Какую желаемую цену Вы имеете в виду?",
        reply_markup=ReplyKeyboardMarkup(
            resize_keyboard=True,
            selective=True,
            keyboard=[
                [KeyboardButton(text="1-3 млн.")],
                [KeyboardButton(text="3-5 млн.")],
                [KeyboardButton(text="5-10 млн.")],
                [KeyboardButton(text="10+ млн.")],
            ]
        )
    )


@router.message(Form.price)
async def price_handler(message: Message, state: FSMContext):
    """
    Обработчик цены
    """
    await state.update_data(price=message.text)
    await state.set_state(Form.phone_number)

    await message.answer("Ваш номер телефона? Он нужен нам для связи с Вами.",
                         reply_markup=ReplyKeyboardRemove())


@router.message(Form.phone_number)
async def phone_number_handler(message: Message, state: FSMContext):
    """
    Обработчик номера телефона
    """
    await state.update_data(phone_number=message.text)

    await message.answer(f"Отлично! Спасибо большое за информацию, <b>{message.from_user.full_name}</b>!\n" +
                         "Я сохраню ваши данные и мы подберем для Вас подходящие варианты жилья.\n\n" +
                         "Наш менеджер свяжется с Вами в ближайшее время.")

    data = await state.get_data()
    await insert_info_to_db(data)
    await state.clear()


@router.message(Command("help"))
async def command_help_handler(message: Message):
    """
    Обработчик команды /help
    """
    help_message = (
        "Мечтаете о новой квартире?\n\n"
        "Наш бот поможет Вам быстро и легко найти идеальное жилье в новостройке!\n\n"
        "<b>Как это работает?</b>\n\n"
        "1. Расскажите боту о своих желаниях:\n"
        "- В каком городе Вы живете?\n"
        "- В каком районе Вы хотите купить квартиру?\n"
        "- Какую площадь Вы ищете?\n"
        "- Какую цену Вы готовы платить?\n"
        "2. Оставьте свои данные, чтобы наш менеджер связался с Вами в кратчайшие сроки.\n\n"
        "3. Специалист подберет для Вас несколько вариантов квартир, ответит на все Ваши вопросы и проведет "
        "сделку.\n\n"
        "<b>Доступные команды:</b>\n\n"
        "/start - Начать опрос для поиска недвижимости\n"
        "/help - Что происходит, помогите\n"
        "/cancel - Отменить действие"
    )
    await message.answer(help_message)


@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Позволяет пользователю отменить любое действие
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)

    await state.clear()

    await message.answer(
        "Вы отменили действие.",
        reply_markup=ReplyKeyboardRemove(),
    )


async def insert_info_to_db(data: Dict):
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


async def main():
    bot = TelegramBot(TOKEN, router)
    await bot.run()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
