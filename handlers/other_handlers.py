from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state

import data
from keyboards.user_keyboards import back_markup
from states.user_states import UserStates


other_handler_router = Router()


@other_handler_router.message(StateFilter(default_state))
async def other(message: Message):
    await message.answer(
        text="Не знаю такого."
    )


@other_handler_router.message(StateFilter(UserStates))
async def incorrect_input(message: Message, state: FSMContext):
    incorrect = "<b>Неправильно!</b>"
    stored_state = await state.get_state()

    if stored_state == UserStates.random_number_input:
        await message.answer(
            text=f"{incorrect}"
                 f"\n\n{data.range_input_text}",
            reply_markup=back_markup
        )

    elif stored_state == UserStates.password_length_input:
        await message.answer(
            text=f"{incorrect}"
                 f"\n\n{data.password_length_input}",
            reply_markup=back_markup
        )

    elif stored_state == UserStates.items_input:
        await message.answer(
            text=f"{incorrect}"
                 f"\n\n{data.items_input_text}",
            reply_markup=back_markup
        )
