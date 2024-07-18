from random import randint, choice

from aiogram import Router, F
from aiogram.filters import (
    CommandStart,
    StateFilter,
    ChatMemberUpdatedFilter,
    IS_MEMBER,
    IS_NOT_MEMBER,
)
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, ChatMemberUpdated
from aiogram.exceptions import TelegramBadRequest

from aiogram_dialog import DialogManager, StartMode

from tgbot.data import *
from tgbot.keyboards.user_keyboards import (
    start_keyboard_func,
    back_markup,
    back_button,
    retry_button,
)
from tgbot.states.user_states import UserStates, StartSG

from database.repo.requests import RequestRepo


router = Router()


@router.message(CommandStart())
async def command_start(
    message: Message,
    state: FSMContext,
    repo: RequestRepo,
    dialog_manager: DialogManager,
):
    # await message.answer(
    #     text=start_text,
    #     reply_markup=start_keyboard_func()
    # )
    #
    await repo.users_actions.create_tg_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )
    #
    # await state.set_state(UserStates.first_state)

    await dialog_manager.start(state=StartSG.start_st, mode=StartMode.RESET_STACK)


@router.message(
    F.text.regexp(r"\d+\s{0,1}-\s{0,1}\d+"), StateFilter(UserStates.random_number_input)
)
async def random_number(
    message: Message, state: FSMContext, retry_button_pressed: bool = False
):
    # :TODO delete

    stored_data = await state.get_data()

    try:
        if not retry_button_pressed:
            await state.update_data({"user_input": message.text})

            num1, num2 = message.text.split("-")

            await message.answer(
                text=f"<b>Випадкове число:</b> <code>{randint(int(num1), int(num2))}</code>"
                f'\n\nЩоб згенерувати ще раз натисніть кнопку <b>"Ще раз 🔄"</b>'
                f"\n<i>Або {range_input_text[:7].lower()} новий {range_input_text[8:]}</i>",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[[retry_button], [back_button]]
                ),
            )

        else:
            num1, num2 = stored_data["user_input"].split("-")

            await message.edit_text(
                text=f"<b>Випадкове число:</b> <code>{randint(int(num1), int(num2))}</code>"
                f'\n\nЩоб згенерувати ще раз натисніть кнопку <b>"Ще раз 🔄"</b>'
                f"\n<i>Або {range_input_text[:7].lower()} новий {range_input_text[8:]}</i>",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[[retry_button], [back_button]]
                ),
            )

    except ValueError:
        await message.answer(
            text=f"<b>Неправильно!</b>"
            f"\n<pre>&lt;число1&gt; має бути менше за &lt;число2&gt;</pre>"
            f"\n\n<i>{range_input_text[:7]} новий {range_input_text[8:]}</i>",
            reply_markup=back_markup,
        )


@router.message(F.text.isdigit(), StateFilter(UserStates.password_length_input))
async def generate_password(
    message: Message, state: FSMContext, retry_button_pressed: bool = False
):
    # :TODO delete

    stored_data = await state.get_data()

    password = ""

    try:

        if not retry_button_pressed:
            await state.update_data({"user_input": message.text})

            password += "".join(choice(symbols) for _ in range(int(message.text)))

            await message.answer(
                text=f"<b>Випадковий пароль:</b> <code>{password}</code>"
                f'\n\nЩоб згенерувати ще раз натисніть кнопку <b>"Ще раз 🔄"</b>'
                f"\n<i>Або {password_length_input[:7].lower()} нову {password_length_input[8:]}</i>",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[[retry_button], [back_button]]
                ),
            )

        else:
            password += "".join(
                choice(symbols) for _ in range(int(stored_data["user_input"]))
            )

            await message.edit_text(
                text=f"<b>Випадковий пароль:</b> <code>{password}</code>"
                f'\n\nЩоб згенерувати ще раз натисніть кнопку <b>"Ще раз 🔄"</b>'
                f"\n<i>Або {password_length_input[:7].lower()} нову {password_length_input[8:]}</i>",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[[retry_button], [back_button]]
                ),
            )

    except TelegramBadRequest:
        await message.answer(
            text=f"<b>Неправильно!</b>"
            f"\nМаксимальна довжина пароля <b>3991</b>"
            f"\n\n<i>{password_length_input[:7]} нову {password_length_input[8:]}</i>",
            reply_markup=back_markup,
        )


@router.message(
    F.text.regexp(r"(\b\w+\b)(,\s\1)*"), StateFilter(UserStates.items_input)
)
async def select_random_item(
    message: Message, state: FSMContext, retry_button_pressed: bool = False
):
    # :TODO remake with dialogs

    stored_data = await state.get_data()

    try:

        if not retry_button_pressed:
            await state.update_data({"user_input": message.text})

            items_list = [
                item if item[0] != " " else item[1:] for item in message.text.split(",")
            ]

            await message.answer(
                text=f"<b>Випадковий елемент:</b> <code>{choice(items_list)}</code>"
                f'\n\nЩоб згенерувати ще раз натисніть кнопку <b>"Ще раз 🔄"</b>'
                f"\n<i>Або {items_input_text[:7].lower()} новий {items_input_text[8:]}</i>",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[[retry_button], [back_button]]
                ),
            )

        else:
            items_list = [
                item if item[0] != " " else item[1:]
                for item in stored_data["user_input"].split(",")
            ]

            await message.edit_text(
                text=f"<b>Випадковий елемент:</b> <code>{choice(items_list)}</code>"
                f'\n\nЩоб згенерувати ще раз натисніть кнопку <b>"Ще раз 🔄"</b>'
                f"\n<i>Або {items_input_text[:7].lower()} новий {items_input_text[8:]}</i>",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[[retry_button], [back_button]]
                ),
            )

    except IndexError:
        await message.answer(
            text=f"<b>Неправильно!</b>"
            f"\nВ кінці останнього елементу не має бути коми!"
            f"\n\n<i>{items_input_text[:7]} новий {items_input_text[8:]}</i>",
            reply_markup=back_markup,
        )


@router.chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
@router.my_chat_member(ChatMemberUpdatedFilter(IS_MEMBER >> IS_NOT_MEMBER))
async def set_user_not_member_status(event: ChatMemberUpdated, repo: RequestRepo):
    await repo.users_actions.change_status(user_id=event.from_user.id, is_active=False)


@router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
@router.my_chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> IS_MEMBER))
async def set_user_member_status(event: ChatMemberUpdated, repo: RequestRepo):
    await repo.users_actions.change_status(user_id=event.from_user.id, is_active=True)
