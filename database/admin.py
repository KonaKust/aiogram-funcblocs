from aiomysql import Pool
from database.connect import db_connect


class Admin:
    pool: Pool = db_connect

    async def list_of_all_users(self):  # Выводим список всех пользоавтелей
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                sql = "SELECT `id`, `username`, `user_id` FROM `users`;"
                await cur.execute(sql)
                users = await cur.fetchall()
                columns = [
                    desc[0] for desc in cur.description
                ]  # получаем описание столбцов
        users_list = [
            dict(zip(columns, user)) for user in users
        ]  # создает пары ключ-значение для каждого кортежа
        return users_list  # в конечном итоге получаем словарь для каждого пользователя
