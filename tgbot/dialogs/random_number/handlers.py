from random import randint
from re import fullmatch

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button

from tgbot.states.user_states import RandomNumberSG


def number_check(numbers_range: str):
    num1, num2 = numbers_range.split("-")

    if fullmatch(pattern=r"\d+\s{0,1}-\s{0,1}\d+", string=numbers_range):
        if int(num1) < int(num2):
            return numbers_range

    raise ValueError


async def generate_random_number(dialog_manager: DialogManager, numbers_range: str = None):
    num1, num2 = numbers_range.split("-")

    random_number = randint(int(num1), int(num2))
    dialog_manager.dialog_data.update(random_number=random_number)


async def retry(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    stored_range = dialog_manager.dialog_data.get("stored_range")

    await generate_random_number(dialog_manager, stored_range)

    await callback.answer("⚠️ Згенеровано")
    await dialog_manager.switch_to(
        state=RandomNumberSG.random_number_generated_st,
        show_mode=ShowMode.EDIT
    )


async def correct_random_number_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    numbers_range: str,
):
    dialog_manager.show_mode = ShowMode.NO_UPDATE

    dialog_manager.dialog_data.update(stored_range=numbers_range)

    await generate_random_number(dialog_manager, numbers_range)

    await dialog_manager.switch_to(
        state=RandomNumberSG.random_number_generated_st,
        show_mode=ShowMode.SEND
    )


async def error_random_number_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    error: ValueError,
):
    await dialog_manager.switch_to(
        state=RandomNumberSG.random_number_error_st,
        show_mode=ShowMode.SEND
    )
