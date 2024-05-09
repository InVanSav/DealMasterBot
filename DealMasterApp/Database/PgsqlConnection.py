from DealMasterApp.ConfigParser import ConfigParser


class PgsqlConnection:
    def __init__(self, config_parser: ConfigParser):
        self.config_parser = config_parser

    def get_db_url(self):
        """
        Возвращает строку подключения к БД из конфигурации.
        """
        user = self.config_parser.get_value("Database", "User")
        password = self.config_parser.get_value("Database", "Password")
        database = self.config_parser.get_value("Database", "Database")
        host = self.config_parser.get_value("Database", "Host")

        return f"dbname={database} user={user} password={password} host={host}"
