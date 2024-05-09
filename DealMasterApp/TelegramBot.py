from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


class TelegramBot:
    def __init__(self, token: str, router: Router):
        self.token = token
        self.router = router
        self.dp = Dispatcher()

    async def run(self):
        bot = Bot(
            token=self.token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML))

        self.dp.include_router(self.router)

        await self.dp.start_polling(bot)
