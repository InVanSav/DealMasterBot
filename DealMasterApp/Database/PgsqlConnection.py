from DealMasterApp.ConfigParser import ConfigParser


class PgsqlConnection:
    """ Класс для установления соединения с базой данных PostgreSQL. """

    def __init__(self, config_parser: ConfigParser):
        """
        Инициализирует объект PgsqlConnection.

        Args:
            config_parser (ConfigParser): Объект парсера конфигурационного файла.
        """
        self.config_parser = config_parser

    def get_db_url(self):
        """ Возвращает строку подключения к БД из конфигурации. """
        user = self.config_parser.get_value("Database", "User")
        password = self.config_parser.get_value("Database", "Password")
        database = self.config_parser.get_value("Database", "Database")
        host = self.config_parser.get_value("Database", "Host")

        return f"dbname={database} user={user} password={password} host={host}"
