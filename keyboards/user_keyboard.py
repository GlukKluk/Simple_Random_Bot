from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


StartMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🌀 Випадковість", callback_data="random")],

        [InlineKeyboardButton(text="ℹ️ Про бота", callback_data="about"),
         InlineKeyboardButton(text="🛠 Додатково", callback_data="additionally")]
    ]
)
