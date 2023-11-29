from aiogram import Bot, Dispatcher
from loguru import logger

from config.config_reader import config

# Определение бота
logger.info("Creating Bot and Dispatcher")
bot = Bot(token=config.bot_token.get_secret_value())
dp_main = Dispatcher()


def startModules():  # Запуск модулей
    try:
        logger.info("Start loading modules...")
        from bot.core import loader as core

        core.enable()

        logger.info("Module loading completed!")
    except Exception:
        logger.exception


startModules()
