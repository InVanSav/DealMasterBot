import aiopg

from DealMasterApp.Database.PgsqlConnection import PgsqlConnection


class PgsqlHandler:
    """ Класс для работы с базой данных PostgreSQL. """

    def __init__(self, pgsql_connection: PgsqlConnection):
        """
        Инициализирует объект PgsqlHandler.

        Args:
            pgsql_connection (PgsqlConnection): Объект для подключения к базе данных.
        """
        self.db_url = pgsql_connection.get_db_url()

    async def execute_sql_script_async(self, sql_script_path: str, params: any):
        """
        Выполняет SQL-скрипт и передает ему параметры.

        Args:
            sql_script_path (str): Путь к SQL-скрипту.
            params (dict): Словарь параметров для скрипта.
        """
        try:
            async with aiopg.connect(self.db_url) as conn:
                async with conn.cursor() as cur:
                    with open(sql_script_path, "r") as f:
                        sql_query = f.read()
                    await cur.execute(sql_query, params)
        except Exception as e:
            print(f"Ошибка при выполнении SQL-скрипта: {e}")

    async def select_sql_script_async(self, sql_script_path: str, params: any):
        """
        Выполняет SELECT-запрос и возвращает результат.

        Args:
            sql_script_path (str): Путь к SQL-скрипту.
            params (dict): Словарь параметров.

        Returns:
            list[tuple]: Список результатов запроса.
        """
        try:
            async with aiopg.connect(self.db_url) as conn:
                async with conn.cursor() as cur:
                    with open(sql_script_path, "r") as f:
                        sql_query = f.read()
                    await cur.execute(sql_query, params)

                    return await cur.fetchall()
        except Exception as e:
            print(f"Ошибка при выполнении SELECT-запроса: {e}")
            return []
