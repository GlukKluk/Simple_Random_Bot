from aiogram_dialog import DialogManager


async def get_password(dialog_manager: DialogManager, **kwargs):
    password = dialog_manager.dialog_data.get("password")

    return {
        "password": password
    }
