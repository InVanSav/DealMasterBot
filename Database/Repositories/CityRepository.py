from Database.PgsqlHandler import PgsqlHandler


class CityRepository:
    """Класс для работы с городами в базе данных."""

    def __init__(self, pgsql_handler: PgsqlHandler, scripts_path: str):
        """
        Инициализация объекта CityRepository.

        Аргументы:
            pgsql_handler (PgsqlHandler): обработчик для работы с PostgreSQL.
            scripts_path (str): путь к директории со скриптами.
        """
        self.pgsql_handler = pgsql_handler
        self.scripts_path = scripts_path

    async def get_cities_async(self):
        """ Получает города из базы данных асинхронно. """
        try:
            cities = await self.pgsql_handler.select_sql_script_async(
                sql_script_path=self.scripts_path + "/select_all.sql",
                params=None,
            )

            list_result = [item for sublist in cities for item in sublist]

            return list_result
        except Exception as e:
            print(f"Ошибка при получении городов: {e}")
