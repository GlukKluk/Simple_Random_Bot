from .start.dialogs import start_dialog
from .randomness.dialogs import randomness_dialog
from .random_number.dialogs import random_number_dialog


dialogs_list = [
    start_dialog,
    randomness_dialog,
    random_number_dialog,
]

__all__ = [
    "dialogs_list"
]
