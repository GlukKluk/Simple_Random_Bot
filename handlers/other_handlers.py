from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import StateFilter

from data import *
from keyboards.user_keyboards import back_markup
from states.user_states import UserStates


router = Router()


@router.message(StateFilter(UserStates))
async def incorrect_input(message: Message, state: FSMContext):
    incorrect = "<b>Неправильно!</b>"
    stored_state = await state.get_state()

    if stored_state == UserStates.random_number_input:
        await message.answer(
            text=f"{incorrect}"
                 f"\n\n{range_input_text}",
            reply_markup=back_markup
        )

    elif stored_state == UserStates.password_length_input:
        await message.answer(
            text=f"{incorrect}"
                 f"\n\n{password_length_input}",
            reply_markup=back_markup
        )

    elif stored_state == UserStates.items_input:
        await message.answer(
            text=f"{incorrect}"
                 f"\n\n{items_input_text}",
            reply_markup=back_markup
        )

    elif stored_state == UserStates.roll_the_dice_state:
        await message.answer(
            text=f"Не знаю такого.",
            reply_markup=back_markup
        )

        await state.set_state(UserStates.first_state)

    else:
        await message.answer(
            text="Не знаю такого."
        )
