from aiogram import Router
from aiogram.types import Message
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state


other_handler_router = Router()


@other_handler_router.message(StateFilter(default_state))
async def other(message: Message):
    await message.answer(
        text="Не знаю такого."
    )
