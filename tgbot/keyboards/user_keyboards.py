from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_keyboard_func(is_admin=False):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🌀 Випадковість", callback_data="randomness")],

            [InlineKeyboardButton(text="ℹ️ Про бота", callback_data="about"),
             InlineKeyboardButton(text="🛠 Додатково", callback_data="additionally")]
        ]
    )

    if is_admin:
        keyboard.inline_keyboard.append(
            [InlineKeyboardButton(text="📊 Статистка", callback_data="statistic")]
        )

    return keyboard


back_button = InlineKeyboardButton(text="⬅️ Назад", callback_data="back")

retry_button = InlineKeyboardButton(text="🔄 Ще раз", callback_data="retry")


randomness_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔢 Випадкове число", callback_data="random_number"),
            InlineKeyboardButton(text="🔐 Згенерувати пароль", callback_data="generate_password")
        ],

        [
            InlineKeyboardButton(text="🗃 Випадковий варіант зі списку", callback_data="select_item"),
            InlineKeyboardButton(text="🎲 Кинути кубик", callback_data="roll_the_dice")
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
