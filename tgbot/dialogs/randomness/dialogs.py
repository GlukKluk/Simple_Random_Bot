from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const

from tgbot.states.user_states import RandomnessSG
from .handlers import *
from ..back import back_button

randomness_dialog = Dialog(
    Window(
        Const(text="Вибери потрібну дію, натиснувши на відповідну кнопку що розташована нижче ⬇️"),
        Row(
            Button(
                text=Const("🔢 Випадкове число"),
                id="random_number",
                on_click=switch_to_random_number
            ),
            Button(
                text=Const("🔐 Згенерувати пароль"),
                id="generate_password",
                # on_click=
            )
        ),
        Row(
            Button(
                text=Const("🗃 Випадковий варіант зі списку"),
                id="select_item",
                # on_click=
            ),
            Button(
                text=Const("🎲 Кинути кубик"),
                id="roll_the_dice",
                # on_click=
            )
        ),
        Button(
            text=Const("🧐 Інше"),
            id="other",
            # on_click=
        ),
        back_button,
        state=RandomnessSG.randomness_st
    )
)