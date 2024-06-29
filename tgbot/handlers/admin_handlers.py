from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tgbot.data import start_text
from tgbot.keyboards.user_keyboards import start_keyboard_func
from tgbot.config import load_config
from tgbot.filters.admin_filters import AdminFilter
from tgbot.states.user_states import UserStates
from database.repo.requests import RequestRepo


config = load_config()

router = Router()
router.message.filter(AdminFilter(admins_id=config.tg_connect.admins_id))


@router.message(CommandStart())
async def command_start(message: Message, state: FSMContext, repo: RequestRepo):
    await message.answer(
        text=start_text,
        reply_markup=start_keyboard_func(is_admin=True)
    )

    await repo.users_actions.create_tg_user(
        user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )

    await state.set_state(UserStates.first_state)
