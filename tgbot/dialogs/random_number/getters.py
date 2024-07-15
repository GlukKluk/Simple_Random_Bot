from aiogram_dialog import DialogManager


async def get_random_number(dialog_manager: DialogManager, **kwargs):
    random_number = dialog_manager.dialog_data.get("random_number")

    return {"random_number": random_number}
