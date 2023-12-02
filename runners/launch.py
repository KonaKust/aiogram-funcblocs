from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from loguru import logger

from config.config_reader import config

# Определение бота
logger.info("Creating Bot and Dispatcher")
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode=ParseMode.MARKDOWN_V2)
dp_main = Dispatcher()


def startModules():  # Запуск модулей
    try:
        logger.info("Start loading modules...")
        from bot.admin import loader as adminka
        from bot.core import loader as core

        core.enable()
        adminka.enable()

        logger.info("Module loading completed!")
    except Exception as e:
        logger.error(f"Error when import: {e}")


startModules()
