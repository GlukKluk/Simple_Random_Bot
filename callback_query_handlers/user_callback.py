from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import CallbackQuery, InlineKeyboardMarkup

import data
from keyboards.user_keyboards import start_markup, randomness_markup, back_markup, retry_button, back_button
from states.user_states import UserStates


user_callback_router = Router()


@user_callback_router.callback_query(F.data == "randomness", StateFilter(UserStates.first_state))
async def randomness(callback: CallbackQuery, state: FSMContext):
    await state.update_data(
        {"stored_data": data.user_datas[0]}
    )

    await callback.message.edit_text(
        text=data.randomness_SelectButton_text,
        reply_markup=randomness_markup
    )


@user_callback_router.callback_query(F.data == "about", StateFilter(UserStates.first_state))
@user_callback_router.callback_query(F.data == "additionally", StateFilter(UserStates.first_state))
async def about(callback: CallbackQuery, state: FSMContext):
    await state.update_data(
        {"stored_data": data.user_datas[0]}
    )

    await callback.message.edit_text(
        text="@@@@@@@@@@@"
             "\n@      <b>В розробці</b>      @"
             "\n@@@@@@@@@@@",
        reply_markup=back_markup
    )


@user_callback_router.callback_query(F.data == "back")
async def back(callback: CallbackQuery, state: FSMContext):
    stored_data = await state.get_data()
    stored_state = await state.get_state()

    if stored_data["stored_data"] == data.user_datas[0]:

        await callback.message.edit_text(
            text=data.start_text,
            reply_markup=start_markup
        )

    elif stored_state == UserStates.roll_the_dice_state:

        await state.update_data(
            {"stored_data": data.user_datas[0]}
        )

        await callback.message.answer(
            text=data.randomness_SelectButton_text,
            reply_markup=randomness_markup
        )

        await callback.answer()

    elif stored_data["stored_data"] == data.user_datas[1]:
        await state.update_data(
            {"stored_data": data.user_datas[0]}
        )

        await callback.message.edit_text(
            text=data.randomness_SelectButton_text,
            reply_markup=randomness_markup
        )

    await state.set_state(UserStates.first_state)


@user_callback_router.callback_query(F.data == "retry")
async def retry(callback: CallbackQuery, state: FSMContext):
    stored_state = await state.get_state()

    if stored_state == UserStates.random_number_input:

        await callback.message.edit_text(
            text=data.range_input_text,
            reply_markup=back_markup
        )

    elif stored_state == UserStates.password_length_input:

        await callback.message.edit_text(
            text=data.password_length_input,
            reply_markup=back_markup
        )

    elif stored_state == UserStates.items_input:

        await callback.message.edit_text(
            text=data.items_input_text,
            reply_markup=back_markup
        )

    elif stored_state == UserStates.roll_the_dice_state:
        await callback.message.answer_dice(
            reply_markup=InlineKeyboardMarkup(
                inline_keyboard=[
                    [retry_button],
                    [back_button]
                ]
            )
        )

        await callback.answer()


@user_callback_router.callback_query(F.data == "random_number", StateFilter(UserStates.first_state))
async def random_number_input(callback: CallbackQuery, state: FSMContext):
    await state.update_data(
        {"stored_data": data.user_datas[1]}
    )

    await state.set_state(UserStates.random_number_input)

    await callback.message.edit_text(
        text=data.range_input_text,
        reply_markup=back_markup
    )


@user_callback_router.callback_query(F.data == "generate_password", StateFilter(UserStates.first_state))
async def generate_password_input(callback: CallbackQuery, state: FSMContext):
    await state.update_data(
        {"stored_data": data.user_datas[1]}
    )

    await state.set_state(UserStates.password_length_input)

    await callback.message.edit_text(
        text=data.password_length_input,
        reply_markup=back_markup
    )


@user_callback_router.callback_query(F.data == "select_item", StateFilter(UserStates.first_state))
async def select_item_input(callback: CallbackQuery, state: FSMContext):
    await state.update_data(
        {"stored_data": data.user_datas[1]}
    )

    await state.set_state(UserStates.items_input)

    await callback.message.edit_text(
        text=data.items_input_text,
        reply_markup=back_markup
    )


@user_callback_router.callback_query(F.data == "roll_the_dice", StateFilter(UserStates.first_state))
async def roll_the_dice(callback: CallbackQuery, state: FSMContext):
    await state.update_data(
        {"stored_data": data.user_datas[1]}
    )

    await state.set_state(UserStates.roll_the_dice_state)

    await callback.message.answer_dice(
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [retry_button],
                [back_button]
            ]
        )
    )

    await callback.answer()


@user_callback_router.callback_query(F.data == "other", StateFilter(UserStates.first_state))
async def other(callback: CallbackQuery, state: FSMContext):
    await state.update_data(
        {"stored_data": data.user_datas[1]}
    )

    await callback.message.edit_text(
        text="@@@@@@@@@@@"
             "\n@      <b>В розробці</b>      @"
             "\n@@@@@@@@@@@",
        reply_markup=back_markup
    )
