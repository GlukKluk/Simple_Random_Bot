from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from tgbot.states.user_states import RandomnessSG, StatisticSG


async def switch_to_randomness(
    callback: CallbackQuery, widget: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(RandomnessSG.randomness_st)

    await dialog_manager.switch_to(RandomnessSG.randomness_st)


async def switch_to_statistic(
    callback: CallbackQuery, widget: Button, dialog_manager: DialogManager
):
    await dialog_manager.start(StatisticSG.statistics_st)

    await dialog_manager.switch_to(StatisticSG.statistics_st)
