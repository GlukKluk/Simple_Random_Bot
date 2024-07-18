from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, SwitchTo
from aiogram_dialog.widgets.text import Const, Format

from tgbot.states.user_states import RandomNumberSG

from .getters import get_random_number
from .handlers import (
    number_check,
    retry,
    clear_stored_range,
    correct_random_number_handler,
    error_random_number_handler,
)
from ..back import back_button

random_number_dialog = Dialog(
    Window(
        Const(
            text="Введіть діапазон у форматі:"
                 "\n<pre>&lt;число1&gt; - &lt;число2&gt;</pre>"
        ),
        TextInput(
            id="random_number_input",
            type_factory=number_check,
            on_success=correct_random_number_handler,
            on_error=error_random_number_handler,
        ),
        back_button,
        state=RandomNumberSG.random_number_input_st,
    ),
    Window(
        Format(
            text="<b>Випадкове число:</b> <code>{random_number}</code>"
                 '\n\nЩоб згенерувати ще раз натисніть кнопку <b>"🔄 Ще раз"</b>"'
        ),
        SwitchTo(
            text=Const("✏️ Новий діапазон"),
            id="new_range",
            state=RandomNumberSG.random_number_input_st,
            on_click=clear_stored_range,
        ),
        Button(text=Const("Ще раз 🔄"), id="retry", on_click=retry),
        back_button,
        state=RandomNumberSG.random_number_generated_st,
        getter=get_random_number,
    ),
    Window(
        Const(
            text="<b>Неправильно!</b>"
                 "\nВведіть діапазон у форматі:"
                 "\n<pre>&lt;число1&gt; - &lt;число2&gt;</pre>"
        ),
        TextInput(
            id="random_number_input",
            type_factory=number_check,
            on_success=correct_random_number_handler,
            on_error=error_random_number_handler,
        ),
        back_button,
        state=RandomNumberSG.random_number_error_st,
    ),
)
