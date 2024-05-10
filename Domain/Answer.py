from typing import NamedTuple
from uuid import UUID


class Answer(NamedTuple):
    answer_id: UUID
    user_id: UUID
    city: str
    district: str
    area: str
    price: str
