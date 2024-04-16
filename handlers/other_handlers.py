from aiogram import Router
from aiogram.types import Message


other_handler_router = Router()


@other_handler_router.message()
async def other(message: Message):
    await message.answer(
        text="Не знаю такого."
             "\nБудь-ласка використовуй кнопки."
    )
