# from aiohttp import web
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

# from aiogram.types import Update
from aiogram.fsm.storage.redis import RedisStorage
from loguru import logger

from config.config_reader import config

# Определение бота
logger.info("Creating Bot and Dispatcher")

token = config.bot_token.get_secret_value()
# ngrok_uri = config.ngrok_uri.get_secret_value()
# ngrok_uri = "https://5485-185-75-65-10.ngrok-free.app"
storage = RedisStorage.from_url(
    "redis://localhost:6379/0",
)
bot = Bot(token, parse_mode=ParseMode.MARKDOWN_V2)
dp_main = Dispatcher(storage=storage)
# app = web.Application()
#
# webhook_path = f"/{token}"
#
#
# async def set_webhook():
#     webhook_uri = f"{ngrok_uri}{webhook_path}"
#     await bot.set_webhook(webhook_uri)
#
#
# async def handle_webhook(request):
#     url = str(request.url)
#     index = url.rfind("/")
#     token = url[index + 1 :]
#
#     if token == token:
#         request_data = await request.json()
#         update = Update.model_validate(request_data)
#
#         await dp_main.feed_update(update=update, bot=bot)
#
#         return web.Response()
#     else:
#         return web.Response(status=403)
#
#
# app.router.add_post(f"/{token}", handle_webhook)


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
