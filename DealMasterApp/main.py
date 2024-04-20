import asyncio
import os
import uuid

from Database.PgsqlConnection import PgsqlConnection
from Database.PgsqlHandler import PgsqlHandler
from Database.Repositories.UserRepository import UserRepository
from Database.Repositories.AnswerRepository import AnswerRepository
from DealMasterApp.ConfigParser import ConfigParser
from DealMasterApp.Domain.Answer import Answer
from DealMasterApp.Domain.User import User

project_absolute_path = os.path.dirname(__file__)

config_path = os.path.join(project_absolute_path, 'config.ini')

user_scripts_path = os.path.join(project_absolute_path, 'Database/Scripts/User')
answer_scripts_path = os.path.join(project_absolute_path, 'Database/Scripts/Answer')

config_parser = ConfigParser(config_path)
connection_data = PgsqlConnection(config_parser)
db_handler = PgsqlHandler(connection_data)

user_repository = UserRepository(db_handler, user_scripts_path)
answer_repository = AnswerRepository(db_handler, answer_scripts_path)

user = User(str(uuid.uuid4()), 'John', 'Doe', '89999999999', str(True))
answer = Answer(str(uuid.uuid4()), user.user_id, 'Question 1', 'Question 2', 'Question 3', 'Question 4')


async def main():
    await user_repository.create_user_async(user)
    await answer_repository.create_answer_async(answer)


asyncio.run(main())
