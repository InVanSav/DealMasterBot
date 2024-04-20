import aiopg

from DealMasterApp.Database.PgsqlConnection import PgsqlConnection


class PgsqlHandler:
    def __init__(self, pgsql_connection: PgsqlConnection):
        self.db_url = pgsql_connection.get_db_url()

    async def execute_sql_script_async(self, sql_script_path, params):
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
