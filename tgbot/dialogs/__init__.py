from .start.dialogs import start_dialog

from .randomness.dialogs import randomness_dialog
from .statistic.dialogs import statistic_dialog

from .random_number.dialogs import random_number_dialog
from .generate_password.dialogs import generate_password_dialog
from .select_item.dialogs import select_item_dialog

from .in_development.dialogs import in_development_dialog


dialogs_list = [
    start_dialog,

    randomness_dialog,
    statistic_dialog,

    random_number_dialog,
    generate_password_dialog,
    select_item_dialog,

    in_development_dialog
]

__all__ = ["dialogs_list"]
