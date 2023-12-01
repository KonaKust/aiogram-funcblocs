from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger
import database.admin as admin_db  # Импортируем класс (ещё не изучено)


global db
router = Router()
db = admin_db.Admin()


@router.message(Command("users_list"))  # Список пользователей
async def cmd_user_list(message: Message):
    logger.info("Users_list command handled!")
    users = await db.list_of_all_users()
    response_text = "Список пользователей:\n"
    for user in users:
        response_text += (
            f"\#{user ['id']} \- {user['username']} \(ID: {user['user_id']}\)\n"
        )
    await message.answer(response_text)
    logger.info("Users list sended")


@router.message(Command("count_users"))
async def cmd_count_users(message: Message):
    logger.info("Count_users command handled")
    counts = await db.count_users()
    response_text = f"""
        *Информация о колличестве пользователей*
        Всего: 
        {counts ['total_users']}
        Susbscribe Time:
        {counts ['admin_users']}
        Админов \- {counts ['subscribed_users']}
    """
    await message.answer(response_text)
    logger.info("Counts of users sended")
