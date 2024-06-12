import uuid

from DIContainer import district_repository, city_repository


async def get_available_cities() -> list:
    return await city_repository.get_cities_async()


async def get_volgograd_districts() -> list:
    volgograd_id = uuid.UUID("e1389007-141c-4f43-9a03-1ddb8c153b32")
    return await district_repository.get_districts_async(volgograd_id)


async def get_saint_petersburg_districts() -> list:
    saint_petersburg_id = uuid.UUID("bdbc5317-ea1f-492c-ade4-d0f5c018e00e")
    return await district_repository.get_districts_async(saint_petersburg_id)


def get_invalid_parameter_str(invalid_parameter: str) -> str:
    return f"{invalid_parameter}! Попробуйте ещё раз.\n" \
           "Используйте клавиатуру для ввода ответа.\n"


available_districts = [
    "Ворошиловский",
    "Советский",
    "Тракторозаводский",
    "Центральный",
    "Невский",
    "Московский",
    "Курортный",
    "Красногвардейский",
    "Колпинский",
]

available_cities = [
    "Волгоград",
    "Санкт-Петербург",
]

available_prices = [
    "1-3 млн.",
    "3-5 млн.",
    "5-10 млн.",
    "10+ млн.",
]

available_areas = [
    "До 50 м²",
    "50-100 м²",
    "100+ м²",
]
