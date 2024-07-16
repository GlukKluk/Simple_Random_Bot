from aiogram.types import User
from aiogram_dialog import DialogManager


async def is_admin_getter(
    dialog_manager: DialogManager, event_from_user: User, admin_ids: list, **kwargs
):
    is_admin = event_from_user.id in admin_ids

    return {"is_admin": is_admin}
