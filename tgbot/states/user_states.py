from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    first_state = State()

    random_number_input = State()
    password_length_input = State()
    items_input = State()
    roll_the_dice_state = State()


class StartSG(StatesGroup):
    start = State()


class RandomnessSG(StatesGroup):
    start = State()
