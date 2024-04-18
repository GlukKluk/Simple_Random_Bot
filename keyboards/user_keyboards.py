from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


back_button = InlineKeyboardButton(text="🔙 Назад", callback_data="back")

start_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🌀 Випадковість", callback_data="randomness")],

        [InlineKeyboardButton(text="ℹ️ Про бота", callback_data="about"),
         InlineKeyboardButton(text="🛠 Додатково", callback_data="additionally")]
    ]
)

randomness_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔢 Випадкове число", callback_data="random_number"),
            InlineKeyboardButton(text="🔐 Згенерувати пароль", callback_data="generate_password")
        ],

        [
            InlineKeyboardButton(text="🗃 Випадковий варіант зі списку", callback_data="select_item"),
            InlineKeyboardButton(text="🤩 Випадкова емоджі", callback_data="send_emoji")
        ],

        [
            InlineKeyboardButton(text="🧐 Інше", callback_data="other")
        ],

        [
            back_button
        ]
    ]
)

back_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [back_button]
    ]
)
