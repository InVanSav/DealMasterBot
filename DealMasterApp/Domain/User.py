from typing import NamedTuple
from uuid import UUID


class User(NamedTuple):
    user_id: UUID
    first_name: str
    last_name: str
    phone_number: str
    from_bot: bool
