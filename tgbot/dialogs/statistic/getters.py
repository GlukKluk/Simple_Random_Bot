from aiogram_dialog import DialogManager

from database.repo.requests import RequestRepo


async def get_statistics(dialog_manager: DialogManager, repo: RequestRepo, **kwargs):
    users = await repo.users_actions.get_users()

    count_users = len(users)
    count_active_users = 0

    for user in users:
        if user.is_active:
            count_active_users += 1

    return {
        "count_users": count_users,
        "count_active_users": count_active_users,
        "count_deactivated_users": count_users - count_active_users,
    }
