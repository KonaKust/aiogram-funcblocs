import asyncio
import sys
# import logging

from loguru import logger

from runners.launch import (
    bot,
    dp_main as dp,
)  # Импортируем экземпляры бота и диспетчера


loop = asyncio.get_event_loop()  # Ссылка на текущий цикл событий
logger.info("dp_main --> dp")


async def main() -> None:  # Запуск бота
    logger.add(sys.stderr, level="INFO")
    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("Start Polling")
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    logger.info("Start bot")
    loop.run_until_complete(main())
