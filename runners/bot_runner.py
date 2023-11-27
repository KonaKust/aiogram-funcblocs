async def start_polling(bot, dp) -> None:
    await dp.start_polling(bot, skip_updates=True)
