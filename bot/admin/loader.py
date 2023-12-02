from loguru import logger
from bot.admin.handlers import admin_panel
from runners.launch import dp_main as dp


def enable() -> None:  # Регестрация Роутеров
    dp.include_routers(admin_panel.router)
    logger.info("Admin routers included")
