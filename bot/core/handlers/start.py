from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
import database.user as user_db  # Импортируем класс (ещё не изучено)

router = Router()


@router.message(CommandStart())  # Ловим команду '/start'
async def command_start_handler(message: Message) -> None:
    db = user_db.Users()  # создаём алиас на метод класса?
    user = message.from_user
    if await db.search_user(user.id):
        await message.answer("С возвращением!")
    else:
        await db.add_user(user)  # Добовлем пользователя в БД, если его там нет
        await message.answer("Привет! Добро пожаловать!")
