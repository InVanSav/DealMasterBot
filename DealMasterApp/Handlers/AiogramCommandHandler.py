from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


class AiogramCommandHandler:
    def __init__(self, dp: Dispatcher):
        self.dp = dp

    def register_command(self, command: str, handler):
        """
        Регистрирует новую команду.

        Args:
            command: Название команды (без префикса '/').
            handler: Функция-обработчик команды.
        """
        @self.dp.message(Command(f"{command}"))
        async def command_handler(message: Message):
            await handler(message)
