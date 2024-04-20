from DealMasterApp.Domain import Answer


class AnswerRepository:
    def __init__(self, pgsql_handler, scripts_path):
        self.pgsql_handler = pgsql_handler
        self.scripts_path = scripts_path

    async def create_answer_async(self, answer: Answer):
        """
        Создает новый ответ в базе данных.
        """
        try:
            answer_data = answer.__dict__

            # Удаляем атрибут "_fields", который не нужен для вставки в базу данных
            del answer_data["_fields"]

            await self.pgsql_handler.execute_sql_script_async(
                sql_script_path=self.scripts_path + "/create.sql",
                params=answer_data,
            )
        except Exception as e:
            print(f"Ошибка при создании нового ответа: {e}")
