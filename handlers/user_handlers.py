from random import randint, choice

from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup
from aiogram.fsm.state import default_state

import data
from keyboards.user_keyboards import start_markup, back_button, retry_button
from states.user_states import UserStates


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
    StateFilter(UserStates.random_number_input)
)
async def random_number(message: Message):
    num1, num2 = message.text.split("-")
    random_num = randint(int(num1), int(num2))

    await message.answer(
        text=f"Випадкове число: <code>{random_num}</code>",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [retry_button],
                [back_button]
            ]
        )
    )


@user_handler_router.message(
    F.text.isdigit(),
    StateFilter(UserStates.password_length_input)
)
async def generate_password(message: Message):
    password = ""

    for i in range(int(message.text)):
        password += choice(data.symbols)

    await message.answer(
        text=f"Випадковий пароль: <code>{password}</code>",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [retry_button],
                [back_button]
            ]
        )
    )


@user_handler_router.message(
    F.text.regexp(r"(\b\w+\b)(,\s\1)*"),
    StateFilter(UserStates.items_input)
)
async def select_random_item(message: Message):
    items_list = [item if item[0] != " " else item[1:] for item in message.text.split(",")]

    await message.answer(
        text=f"Випадковий елемент: <code>{choice(items_list)}</code>",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [retry_button],
                [back_button]
            ]
        )
    )
