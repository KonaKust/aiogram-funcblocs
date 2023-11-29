# import asyncio
from loguru import logger
from runners.launch import dp_main as dp
from bot.core.handlers import start, test_types


def enable() -> None:  # Регестрация Роутеров
    dp.include_routers(start.router, test_types.router)
    logger.info("Core routers included!")
