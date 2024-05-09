from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def create_reply_keyboard(button_labels: list[str]) -> ReplyKeyboardMarkup:
    """
    Создает ReplyKeyboardMarkup с указанными кнопками.

    Args:
        button_labels (list[str]): Список строк с названиями кнопок.
    """
    rows = []

    for label in button_labels:
        button = KeyboardButton(text=label)
        rows.append([button])

    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        selective=True,
        keyboard=rows)
