from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager

from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const


async def go_back(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    """
    Ends the current dialogue and returns to the previous dialogue

    :param callback:
    :param widget:
    :param dialog_manager:
    """
    await dialog_manager.done()


back_button: Button = Button(
    text=Const("⬅️ Назад"),
    id="back",
    on_click=go_back
)
