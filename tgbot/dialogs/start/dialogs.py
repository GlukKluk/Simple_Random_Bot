from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const

from tgbot.states.user_states import StartSG
from .getters import is_admin_getter
from .handlers import *

start_dialog = Dialog(
    Window(
        Const(
            text="<b>🤖 Випадковий Бот 🤖</b>"
            "\n\n⚙ Що ж він вміє:"
            "\n🔢 Згенерувати випадкове число"
            "\n🔐 Згенерувати пароль"
            "\n🗃 Вибрати випадковий варіант зі списку"
            "\n🎲 Кинути кубик"
            "\n<u>🔎 І багато іншого</u>"
            "\n\n🔆 Цей бот абсолютно безкоштовний 🔆"
            '\n\n⬇️ Щоб розпочати натисніть <b>"🌀 Випадковість"</b>'
        ),
        Button(
            text=Const(text="🌀 Випадковість"),
            id="randomness",
            on_click=switch_to_randomness,
        ),
        Row(
            Button(
                text=Const(text="ℹ️ Про бота"),
                id="about",
                # on_click=
            ),
            Button(
                text=Const(text="🛠 Додатково"),
                id="additionally",
                # on_click=
            ),
        ),
        Button(
            text=Const("📊 Статистка"),
            id="statistic",
            on_click=switch_to_statistic,
            when="is_admin",
        ),
        state=StartSG.start_st,
        getter=is_admin_getter,
    )
)
