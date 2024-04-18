from aiogram import Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import default_state

from keyboards.user_keyboards import start_markup
import data


user_handler_router = Router()


@user_handler_router.message(CommandStart(), StateFilter(default_state))
async def command_start(message: Message, state: FSMContext):
    await message.answer(
        text=data.start_text,
        reply_markup=start_markup
    )

    await state.update_data(
        {"stored_data": data.user_datas[0]}
    )
