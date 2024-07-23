from re import fullmatch

from aiogram.types import Message, CallbackQuery

from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button

from tgbot.states.user_states import SelectItemSG


def items_check(text: str):
    if fullmatch(pattern=r"(\b\w+\b)(,\s\1)*", string=text):
        return text


async def select_item(dialog_manager: DialogManager, text: str = None):
    items_list = [
        item if item[0] != " " else item[1:] for item in text.split(",")
    ]


async def retry(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    stored_items = dialog_manager.dialog_data.get("stored_items")

    await select_item(dialog_manager, stored_items)

    await callback.answer("⚠️ Згенеровано")
    await dialog_manager.switch_to(
        state=SelectItemSG.item_selected_st,
        show_mode=ShowMode.EDIT
    )


async def clear_stored_items(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    dialog_manager.dialog_data.pop("stored_items")


async def correct_select_items_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str,
):
    dialog_manager.show_mode = ShowMode.NO_UPDATE

    stored_items = dialog_manager.dialog_data.get("stored_items")

    if not stored_items:
        dialog_manager.dialog_data.update(stored_items=text)

    await select_item(dialog_manager, text)

    await dialog_manager.switch_to(
        state=SelectItemSG.item_selected_st,
        show_mode=ShowMode.SEND
    )


async def error_select_items_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        error: ValueError,
):
    await dialog_manager.switch_to(
        state=SelectItemSG.item_error_st,
        show_mode=ShowMode.SEND
    )
