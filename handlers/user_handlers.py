from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.user_keyboard import StartMarkup


user_handler_router = Router()


@user_handler_router.message(CommandStart())
async def command_start(message: Message):
    await message.answer(
        text='🤖 Випадковий Бот 🤖'
             '\n\n⚙ Що ж він вміє:'
             '\n🔢 Згенерувати випадкове число'
             '\n🔐 Згенерувати пароль'
             '\n🗃 Вибрати випадковий варіант зі списку'
             '\n🤩 Надіслати випадкову Telegram емоджі'
             '\n🎲 Кинути кубик'
             '\n\n🔆 Цей бот абсолютно безкоштовний 🔆'
             '\n\n⬇️ Щоб розпочати натисніть "🌀 Випадковість"',

        reply_markup=StartMarkup
    )
