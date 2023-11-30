from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger
import database.admin as admin_db  # Импортируем класс (ещё не изучено)

router = Router()


@router.message(Command("users_list"))  # [2]
async def cmd_start(message: Message):
    db = admin_db.Admin()
    logger.info("Users_list command handled!")
    users = await db.list_of_all_users()
    response_text = "Список пользователей:\n"
    for user in users:
        response_text += (
            f"\#{user ['id']} \- {user['username']} \-\-\- \(ID: {user['user_id']}\)\n"
        )
    await message.answer(response_text)
    logger.info("Users list sended")
