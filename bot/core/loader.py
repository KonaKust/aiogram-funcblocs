# import asyncio
from loguru import logger
from runners.launch import dp_main as dp
from bot.core.handlers import start, main_menu


def enable() -> None:  # Регестрация Роутеров
    dp.include_routers(start.router, main_menu.router)
    logger.info("Core routers included")
