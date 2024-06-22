from aiogram.types import Message
from aiogram.filters import Filter


class AdminFilter(Filter):
    def __init__(self, admins_id: list[int]):
        self.admins_id: list[int] = admins_id

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admins_id
