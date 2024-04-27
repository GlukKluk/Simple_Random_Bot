from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    random_number_input = State()
    password_length_input = State()
    items_input = State()
