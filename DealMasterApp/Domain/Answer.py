from typing import NamedTuple
from uuid import UUID


class Answer(NamedTuple):
    answer_id: UUID
    user_id: UUID
    first_question: str
    second_question: str
    third_question: str
    fourth_question: str
