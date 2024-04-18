from random import randint

from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import default_state

import data
from keyboards.user_keyboards import start_markup
from states.user_states import RandomNumberStates


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


@user_handler_router.message(
    F.text.regexp(r"\d+\s{0,1}-\s{0,1}\d+"),
    StateFilter(RandomNumberStates.random_number_input)
)
async def random_number(message: Message):
    num1, num2 = message.text.split("-")
    random_num = randint(int(num1), int(num2))

    await message.answer(
        text=f"Випадкове число: {random_num}"
    )
