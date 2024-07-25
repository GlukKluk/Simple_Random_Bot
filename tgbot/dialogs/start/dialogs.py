from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row, Start
from aiogram_dialog.widgets.text import Const

from tgbot.states.user_states import (
    StartSG,
    RandomnessSG,
    AboutBotSG,
    AdditionallySG,
    StatisticSG
)
from .getters import is_admin_getter

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
        Start(
            text=Const(text="🌀 Випадковість"),
            id="randomness",
            state=RandomnessSG.randomness_st
        ),
        Row(
            Start(
                text=Const(text="ℹ️ Про бота"),
                id="about",
                state=AboutBotSG.about_bot_st  # in process...
            ),
            Start(
                text=Const(text="🛠 Додатково"),
                id="additionally",
                state=AdditionallySG.additionally_st  # in process...
            ),
        ),
        Start(
            text=Const("📊 Статистка"),
            id="statistic",
            state=StatisticSG.statistics_st,
            when="is_admin",
        ),
        state=StartSG.start_st,
        getter=is_admin_getter,
    )
)
