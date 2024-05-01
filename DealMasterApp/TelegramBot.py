from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message

from DealMasterApp.Handlers.AiogramCommandHandler import AiogramCommandHandler


class TelegramBot:
    def __init__(self, token: str):
        self.token = token
        self.dp = Dispatcher()
        self._handle_commands()

    async def command_help_handler(self, message: Message) -> None:
        """
        Обработчик команды /help
        """
        help_message = (
            "Мечтаете о новой квартире?\n\n"
            "Наш бот поможет Вам быстро и легко найти идеальное жилье в новостройке!\n\n"
            "<b>Как это работает?</b>\n\n"
            "1. Расскажите боту о своих желаниях:\n"
            "- В каком районе Вы хотите купить квартиру?\n"
            "- Какую площадь Вы ищете?\n"
            "- Какую цену Вы готовы платить?\n"
            "- Есть ли у Вас какие-то дополнительные пожелания?\n\n"
            "2. Оставьте свой номер телефона, и наш менеджер свяжется с Вами в кратчайшие сроки.\n\n"
            "3. Специалист подберет для Вас несколько вариантов квартир, ответит на все Ваши вопросы и проведет "
            "сделку.\n\n"
            "<b>Доступные команды:</b>\n\n"
            "/start - Начать опрос для поиска недвижимости\n"
            "/help - Что происходит, помогите"
        )
        await message.answer(help_message)

    async def command_start_handler(self, message: Message) -> None:
        """
        Обработчик команды /start
        """
        await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

    async def run(self):
        bot = Bot(
            token=self.token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML))

        await self.dp.start_polling(bot)

    def _handle_commands(self):
        command_handler = AiogramCommandHandler(self.dp)

        command_handler.register_command("start", self.command_start_handler)
        command_handler.register_command("help", self.command_help_handler)
