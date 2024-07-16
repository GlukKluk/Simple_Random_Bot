from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format


from tgbot.dialogs.back import back_button
from tgbot.states.user_states import StatisticSG

from .getters import get_statistics


statistic_dialog = Dialog(
    Window(
        Format(
            "👥 Загальна кількість користувачів: {count_users}"
            "\n🔊 Активні користувачі: {count_active_users}"
            "\n🔇 Неактивні користувачі: {count_deactivated_users}"
        ),
        back_button,
        state=StatisticSG.statistics_st,
        getter=get_statistics,
    )
)
