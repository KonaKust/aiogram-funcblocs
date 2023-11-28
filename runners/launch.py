from aiogram import Bot, Dispatcher
from loguru import logger

from config.config_reader import config

# Определение бота
bot = Bot(token=config.bot_token.get_secret_value())
logger.info("init dp_main")
dp_main = Dispatcher()


def startModules():  # Запуск модулей
    try:
        logger.info("loading modules...")
        from bot.core import loader as core

        core.enable()

        logger.info("successfully!")
    except Exception:
        logger.exception


startModules()
