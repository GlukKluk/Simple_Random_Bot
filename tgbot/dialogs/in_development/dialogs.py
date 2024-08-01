from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Cancel

from tgbot.states.user_states import InDevelopmentSG


in_development_dialog = Dialog(
    Window(
        Const(
            text="@@@@@@@@@@@"
                 "\n@      <b>В розробці</b>      @"
                 "\n@@@@@@@@@@@"
        ),
        Cancel(
            text=Const("⬅️ Назад"),
            id="back",
        ),
        state=InDevelopmentSG.in_development_st,
    )
)
