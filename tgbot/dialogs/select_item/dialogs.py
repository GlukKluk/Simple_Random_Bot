from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import SwitchTo, Button, Cancel
from aiogram_dialog.widgets.text import Const, Format

from tgbot.states.user_states import SelectItemSG

from .getters import get_item
from .handlers import (
    items_check,
    retry,
    clear_stored_items,
    correct_select_items_handler,
    error_select_items_handler,
)


select_item_dialog = Dialog(
    Window(
        Const(
            text="Введіть список значень у форматі:"
                 "\n<pre>&lt;значення1, значення2, значення3, ... значення&gt;</pre>"
        ),
        TextInput(
            id="select_item_input",
            type_factory=items_check,
            on_success=correct_select_items_handler,
            on_error=error_select_items_handler,
        ),
        Cancel(
            text=Const("⬅️ Назад"),
            id="back",
        ),
        state=SelectItemSG.items_input_st,
    ),
    Window(
        Format(
            text="<b>Випадковий елемент:</b> <code>{item}</code>"
                 '\n\nЩоб згенерувати ще раз натисніть кнопку <b>"🔄 Ще раз"</b>'
                 "\nАбо введіть новий список значень у форматі:"
                 "\n<pre>&lt;значення1, значення2, значення3, ... значення&gt;</pre>"
        ),
        TextInput(
            id="select_item_input",
            type_factory=items_check,
            on_success=correct_select_items_handler,
            on_error=error_select_items_handler,
        ),
        Button(
            text=Const("🔄 Ще раз"),
            id="retry",
            on_click=retry,
        ),
        Cancel(
            text=Const("⬅️ Назад"),
            id="back",
        ),
        state=SelectItemSG.item_selected_st,
        getter=get_item,
    ),
    Window(
        Const(text="<b>Неправильно!</b>"),
        TextInput(
            id="select_item_input",
            type_factory=items_check,
            on_success=correct_select_items_handler,
            on_error=error_select_items_handler,
        ),
        Cancel(
            text=Const("⬅️ Назад"),
            id="back",
        ),
        state=SelectItemSG.item_error_st,
    ),
)
