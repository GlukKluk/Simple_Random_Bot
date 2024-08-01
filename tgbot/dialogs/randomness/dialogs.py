from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start, Button, Row, Cancel
from aiogram_dialog.widgets.text import Const

from tgbot.states.user_states import (
    RandomnessSG,

    RandomNumberSG,
    GeneratePasswordSG,
    SelectItemSG,

    InDevelopmentSG
)


randomness_dialog = Dialog(
    Window(
        Const(
            text="Вибери потрібну дію, натиснувши на відповідну кнопку що розташована нижче ⬇️"
        ),
        Row(
            Start(
                text=Const("🔢 Випадкове число"),
                id="random_number",
                state=RandomNumberSG.random_number_input_st,
            ),
            Start(
                text=Const("🔐 Згенерувати пароль"),
                id="generate_password",
                state=GeneratePasswordSG.password_length_input_st
            ),
        ),
        Row(
            Start(
                text=Const("🗃 Випадковий варіант зі списку"),
                id="select_item",
                state=SelectItemSG.items_input_st
            ),
            Start(  # :TODO not realized (in process)
                text=Const("🎲 Кинути кубик"),
                id="roll_the_dice",
                state=InDevelopmentSG.in_development_st
                # on_click=,
            ),
        ),
        Start(
            text=Const("🧐 Інше"),
            id="other",
            state=InDevelopmentSG.in_development_st
        ),
        Cancel(
            text=Const("⬅️ Назад"),
            id="back",
        ),
        state=RandomnessSG.randomness_st,
    )
)
