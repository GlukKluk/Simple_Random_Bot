from random import choice
from string import ascii_letters, digits

from aiogram.types import CallbackQuery, Message

from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button

from tgbot.states.user_states import GeneratePasswordSG


SYMBOLS = list(ascii_letters + digits + "/!#$%&?@:;-")


def password_check(text: str):
    if text.isdigit():
        if int(text) <= 4000:
            return text

    raise ValueError


async def generate_password(dialog_manager: DialogManager, text: str = None):
    password = ""

    password += "".join(choice(SYMBOLS) for _ in range(int(text)))
    dialog_manager.dialog_data.update(password=password)


async def retry(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    stored_length = dialog_manager.dialog_data.get("stored_length")

    await generate_password(dialog_manager, stored_length)

    await callback.answer("⚠️ Згенеровано")
    await dialog_manager.switch_to(
        state=GeneratePasswordSG.password_generated_st,
        show_mode=ShowMode.EDIT
    )


async def clear_stored_length(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data.pop("stored_length")


async def correct_generate_password_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str,
):
    dialog_manager.show_mode = ShowMode.NO_UPDATE

    stored_length = dialog_manager.dialog_data.get("stored_length")

    if not stored_length:
        dialog_manager.dialog_data.update(stored_length=text)

    await generate_password(dialog_manager, text)

    await dialog_manager.switch_to(
        state=GeneratePasswordSG.password_generated_st,
        show_mode=ShowMode.SEND
    )


async def error_generate_password_handler(
    message: Message,
    widget: ManagedTextInput,
    dialog_manager: DialogManager,
    error: ValueError,
):
    await dialog_manager.switch_to(
        state=GeneratePasswordSG.password_error_st,
        show_mode=ShowMode.SEND
    )
