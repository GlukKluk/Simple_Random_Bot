from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from tgbot.states.user_states import RandomnessSG


async def switch_to_randomness(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    await dialog_manager.start(RandomnessSG.start)

    await dialog_manager.switch_to(RandomnessSG.start)
