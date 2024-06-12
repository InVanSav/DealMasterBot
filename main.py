import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from DIContainer import TOKEN
from Handlers.Commands import EndPollingCommands, AreaCommands, DistrictsCommands, CommonCommands, PhoneNumberCommands, \
    PriceCommands


async def main():
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(EndPollingCommands.router)
    dp.include_router(AreaCommands.router)
    dp.include_router(PhoneNumberCommands.router)
    dp.include_router(DistrictsCommands.router)
    dp.include_router(PriceCommands.router)

    dp.include_router(CommonCommands.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
