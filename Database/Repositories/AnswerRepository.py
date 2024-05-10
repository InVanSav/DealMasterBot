from Database.PgsqlHandler import PgsqlHandler
from Domain import Answer


class AnswerRepository:
    """Класс для работы с ответами в базе данных."""

    def __init__(self, pgsql_handler: PgsqlHandler, scripts_path: str):
        """
        Инициализация объекта AnswerRepository.

        Аргументы:
            pgsql_handler (PgsqlHandler): обработчик для работы с PostgreSQL.
            scripts_path (str): путь к директории со скриптами.
        """
        self.pgsql_handler = pgsql_handler
        self.scripts_path = scripts_path

    async def create_answer_async(self, answer: Answer):
        """
        Создает новый ответ в базе данных асинхронно.

        Аргументы:
            answer (Answer): объект ответа для добавления в БД.
        """
        try:
            await self.pgsql_handler.execute_sql_script_async(
                sql_script_path=self.scripts_path + "/create.sql",
                params=answer,
            )
        except Exception as e:
            print(f"Ошибка при создании нового ответа: {e}")
