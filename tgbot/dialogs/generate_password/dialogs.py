from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import SwitchTo, Button
from aiogram_dialog.widgets.text import Const, Format

from tgbot.states.user_states import GeneratePasswordSG

from .getters import get_password
from .handlers import (
    password_check,
    retry,
    clear_stored_length,
    correct_generate_password_handler,
    error_generate_password_handler,
)
from ..back import back_button


generate_password_dialog = Dialog(
    Window(
        Const(text="Введіть довжину пароля:"),
        TextInput(
            id="password_length_input",
            type_factory=password_check,
            on_success=correct_generate_password_handler,
            on_error=error_generate_password_handler,
        ),
        back_button,
        state=GeneratePasswordSG.password_length_input_st,
    ),
    Window(
        Format(
            text="<b>Випадковий пароль:</b> <code>{password}</code>"
                 '\n\nЩоб згенерувати ще раз натисніть кнопку <b>"🔄 Ще раз"</b>'
        ),
        SwitchTo(
            text=Const("✏️ Нова довжина"),
            id="new_length",
            state=GeneratePasswordSG.password_length_input_st,
            on_click=clear_stored_length,
        ),
        Button(text=Const("🔄 Ще раз"), id="retry", on_click=retry),
        back_button,
        state=GeneratePasswordSG.password_length_generated_st,
        getter=get_password,
    ),
    Window(
        Const(
            text="<b>Неправильно!</b>"
                 "\nВведіть довжину пароля (менше, або рівно 4000):"
        ),
        TextInput(
            id="password_length_input",
            type_factory=password_check,
            on_success=correct_generate_password_handler,
            on_error=error_generate_password_handler,
        ),
        back_button,
        state=GeneratePasswordSG.password_length_error_st
    ),
)
