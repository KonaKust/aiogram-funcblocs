from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from loguru import logger

from config.config_reader import config

# Определение бота
logger.info("Creating Bot and Dispatcher")
storage = RedisStorage.from_url(
    "redis://localhost:6379/0",
)
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.MARKDOWN_V2)
dp_main = Dispatcher(storage=storage)
router = Router()


def startModules():  # Запуск модулей
    try:
        logger.info("Start loading modules...")
        from bot.admin import loader as adminka
        from bot.core import loader as core

        adminka.enable()
        core.enable()  # Ядро должно запускаться последним

        logger.info("Modules loading completed!")
    except Exception as e:
        logger.error(f"Error when import: {e}")


startModules()
dp_main.include_router(router)
