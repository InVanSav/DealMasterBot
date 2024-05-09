import os

from DealMasterApp.ConfigParser import ConfigParser
from DealMasterApp.Database.PgsqlConnection import PgsqlConnection
from DealMasterApp.Database.PgsqlHandler import PgsqlHandler
from DealMasterApp.Database.Repositories.AnswerRepository import AnswerRepository
from DealMasterApp.Database.Repositories.UserRepository import UserRepository

# Путь к файлу конфигурации
project_absolute_path = os.path.dirname(__file__)
config_path = os.path.join(project_absolute_path, 'config.ini')

# Пути к скриптам
user_scripts_path = os.path.join(project_absolute_path, 'Database/Scripts/User')
answer_scripts_path = os.path.join(project_absolute_path, 'Database/Scripts/Answer')

# Подключение к базе данных
config_parser = ConfigParser(config_path)
connection_data = PgsqlConnection(config_parser)
db_handler = PgsqlHandler(connection_data)

# Инициализация репозиториев
user_repository = UserRepository(db_handler, user_scripts_path)
answer_repository = AnswerRepository(db_handler, answer_scripts_path)

# Токен бота
TOKEN = config_parser.get_value("Bot", "Token")