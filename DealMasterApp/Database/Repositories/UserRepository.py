from typing import Dict

from DealMasterApp.Domain import User


class UserRepository:
    def __init__(self, pgsql_handler, scripts_path):
        self.pgsql_handler = pgsql_handler
        self.scripts_path = scripts_path

    async def create_user_async(self, user: User):
        """
        Создает нового пользователя в базе данных.
        """
        try:
            user_data = user.__dict__

            # Удаляем атрибут "_fields", который не нужен для вставки в базу данных
            del user_data["_fields"]

            await self.pgsql_handler.execute_sql_script_async(
                sql_script_path=self.scripts_path + "/create.sql",
                params=user_data,
            )
        except Exception as e:
            print(f"Ошибка при создании нового пользователя: {e}")
