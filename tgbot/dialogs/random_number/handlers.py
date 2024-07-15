from random import randint
from re import fullmatch

from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import ManagedTextInput

from tgbot.states.user_states import RandomNumberSG


def number_check(text: str):
    if fullmatch(
        pattern=r"\d+\s{0,1}-\s{0,1}\d+",
        string=text
    ):
        return text

    raise ValueError


async def correct_random_number_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str
):
    dialog_manager.show_mode = ShowMode.NO_UPDATE

    stored_range = dialog_manager.dialog_data.get("stored_range")

    num1, num2 = text.split("-")

    if not stored_range:
        dialog_manager.dialog_data.update(stored_range=text)

    else:
        num1, num2 = stored_range.split("-")

    random_number = randint(int(num1), int(num2))
    dialog_manager.dialog_data.update(random_number=random_number)

    await dialog_manager.switch_to(state=RandomNumberSG.random_number_generated_st)


async def error_random_number_handler(message: Message, widget: ManagedTextInput, dialog_manager: DialogManager, error: ValueError):
    await message.answer(text=f"<b>Неправильно!</b>")
