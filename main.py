import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher

API_TOKEN = "6804342824:AAGt0TD8ArdX0yq0MByat0rH7wVNI8OX0FA"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


if __name__ == "__main__":
    from runners.bot_runner import start_polling

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start_polling(bot, dp))
