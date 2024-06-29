from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from database.repo.requests import RequestRepo
from tgbot.data import user_datas, start_text
from tgbot.keyboards.user_keyboards import back_markup, start_keyboard_func
from tgbot.states.user_states import UserStates


router = Router()


@router.callback_query(F.data == "statistic", StateFilter(UserStates.first_state))
async def get_statistic(callback: CallbackQuery, state: FSMContext, repo: RequestRepo):
    await state.update_data(
        {"previous_page": user_datas[0]}
    )

    users = await repo.users_actions.get_users()

    count_users = len(users)
    count_active_users = 0

    for user in users:
        if user.is_active:
            count_active_users += 1

    await callback.message.edit_text(
        text=f"👥 Загальна кількість користувачів: {count_users}"
             f"\n🔊 Активні користувачі: {count_active_users}"
             f"\n🔇 Неактивні користувачі: {count_users - count_active_users}",
        reply_markup=back_markup
    )


@router.callback_query(F.data == "back", StateFilter(UserStates))
async def back(callback: CallbackQuery, state: FSMContext):
    stored_data = await state.get_data()

    if stored_data["previous_page"] == user_datas[0]:

        await callback.message.edit_text(
            text=start_text,
            reply_markup=start_keyboard_func(is_admin=True)
        )
