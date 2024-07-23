from aiogram_dialog.dialog import DialogManager


async def get_item(dialog_manager: DialogManager):
    item = dialog_manager.dialog_data.get("item")

    return {
        "item": item
    }
