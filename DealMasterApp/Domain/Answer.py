from typing import NamedTuple
from uuid import UUID


class Answer(NamedTuple):
    answer_id: str
    user_id: str
    first_question: str
    second_question: str
    third_question: str
    fourth_question: str
