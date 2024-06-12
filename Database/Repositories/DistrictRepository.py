from uuid import UUID

from Database.PgsqlHandler import PgsqlHandler


class DistrictRepository:
    """Класс для работы с городами и их районами в базе данных."""

    def __init__(self, pgsql_handler: PgsqlHandler, scripts_path: str):
        """
        Инициализация объекта DistrictRepository.

        Аргументы:
            pgsql_handler (PgsqlHandler): обработчик для работы с PostgreSQL.
            scripts_path (str): путь к директории со скриптами.
        """
        self.pgsql_handler = pgsql_handler
        self.scripts_path = scripts_path

    async def get_districts_async(self, city_id: UUID):
        """
        Получает районы города из базы данных асинхронно.

        Аргументы:
            city_id (str): идентификатор города.
        """
        try:
            districts = await self.pgsql_handler.select_sql_script_async(
                sql_script_path=self.scripts_path + "/select_by_city_id.sql",
                params=(city_id,),
            )

            list_result = [item for sublist in districts for item in sublist]

            return list_result
        except Exception as e:
            print(f"Ошибка при получении списка районов города: {e}")
