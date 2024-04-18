from aiogram.fsm.state import State, StatesGroup


class RandomNumberStates(StatesGroup):
    random_number_input = State()
