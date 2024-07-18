from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from tgbot.states.user_states import RandomNumberSG, GeneratePasswordSG, SelectItemSG, RollTheDiceSG


async def switch_to_random_number(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.start(RandomNumberSG.random_number_input_st)

    await dialog_manager.switch_to(RandomNumberSG.random_number_input_st)


async def switch_to_generate_password(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.start(GeneratePasswordSG.password_length_input_st)

    await dialog_manager.switch_to(GeneratePasswordSG.password_length_input_st)


async def switch_to_select_item(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.start(SelectItemSG.select_item_st)

    await dialog_manager.switch_to(SelectItemSG.select_item_st)


async def switch_to_roll_the_dice(callback: CallbackQuery, widget: Button, dialog_manager: DialogManager):
    await dialog_manager.start(RollTheDiceSG.roll_the_dice_st)

    await dialog_manager.switch_to(RollTheDiceSG.roll_the_dice_st)
