from dataclasses import dataclass

from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    first_state = State()

    random_number_input = State()
    password_length_input = State()
    items_input = State()
    roll_the_dice_state = State()


class StartSG(StatesGroup):
    """
    First level: MAIN MENU
    """

    start_st = State()


class RandomnessSG(StatesGroup):
    """
    Second level: RANDOMNESS MENU
    """

    randomness_st = State()


class RandomNumberSG(StatesGroup):
    """
    Third level: GENERATE RANDOM NUMBER
    """

    random_number_input_st = State()
    random_number_generated_st = State()
    random_number_error_st = State()


class GeneratePasswordSG(StatesGroup):
    """
    Third level: GENERATE PASSWORD
    """

    password_length_input_st = State()
    password_length_generated_st = State()
    password_length_error_st = State()


class SelectItemSG(StatesGroup):
    """
    Third level: SELECT ITEM
    """

    select_item_st = State()
    items_input_st = State()


class RollTheDiceSG(StatesGroup):
    """
    Third level: ROLL THE DICE
    """

    roll_the_dice_st = State()


class AboutBotSG(StatesGroup):
    """
    Second level: ABOUT BOT INFO
    """

    about_bot_st = State()


class AdditionallySG(StatesGroup):
    """
    SECOND level: ADDITIONAL INFO
    """

    additionally_st = State()


class StatisticSG(StatesGroup):
    """
    SECOND level: STATISTICS INFO
    """

    statistics_st = State()

# :TODO test
# @dataclass
# class AllStatesGroup:
#     start: StartSG = StartSG()
#
#     randomness: RandomnessSG = RandomnessSG()
#
#     random_number: RandomNumberSG = RandomNumberSG()
#     generate_password: GeneratePasswordSG = GeneratePasswordSG()
#     select_item: SelectItemSG = SelectItemSG()
#     roll_the_dice: RollTheDiceSG = RollTheDiceSG()
#
#     about: AboutBotSG = AboutBotSG()
#     additionally: AdditionallySG = AdditionallySG()
#
#     statistics: StatisticSG = StatisticSG()
