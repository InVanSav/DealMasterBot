from typing import Dict

from DealMasterApp.Database.PgsqlHandler import PgsqlHandler
from DealMasterApp.Domain import User


class UserRepository:
    """Класс для работы с пользователями в базе данных."""

    def __init__(self, pgsql_handler: PgsqlHandler, scripts_path: str):
        """
        Инициализация объекта UserRepository.

        Аргументы:
            pgsql_handler (PgsqlHandler): обработчик для работы с PostgreSQL.
            scripts_path (str): путь к директории со скриптами.
        """
        self.pgsql_handler = pgsql_handler
        self.scripts_path = scripts_path

    async def create_user_async(self, user: User):
        """
        Создает нового пользователя в базе данных асинхронно.

        Аргументы:
            user (User): объект пользователя для добавления в БД.
        """
        try:
            await self.pgsql_handler.execute_sql_script_async(
                sql_script_path=self.scripts_path + "/create.sql",
                params=user,
            )
        except Exception as e:
            print(f"Ошибка при создании нового пользователя: {e}")
