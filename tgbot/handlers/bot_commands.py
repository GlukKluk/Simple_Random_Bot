from dataclasses import dataclass

from aiogram.types import BotCommand


@dataclass
class UserCommands:
    start: BotCommand = BotCommand(
        command="start",
        description="І почнеться наша розмова!"
    )


@dataclass
class AdminCommands:
    statistic: BotCommand = BotCommand(
        command="statistic",
        description="Статистика бота. ТІЛЬКИ ДЛЯ АДМІНІВ!"
    )
