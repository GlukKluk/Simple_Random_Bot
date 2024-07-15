from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    first_state = State()

    random_number_input = State()
    password_length_input = State()
    items_input = State()
    roll_the_dice_state = State()


class StartSG(StatesGroup):
    start_st = State()


class RandomnessSG(StatesGroup):
    randomness_st = State()


class RandomNumberSG(StatesGroup):
    random_number_input_st = State()
    random_number_generated_st = State()
    random_number_error_st = State()


class GeneratePasswordSG(StatesGroup):
    generate_password_st = State()
    password_length_input_st = State()


class SelectItemSG(StatesGroup):
    select_item_st = State()
    items_input_st = State()


class RollTheDiceSG(StatesGroup):
    roll_the_dice_st = State()
