from typing import Callable, Any, Awaitable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Update

from database.repo.requests import RequestRepo


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, session_pool) -> None:
        self.session_pool = session_pool

    async def __call__(
            self,
            handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any],
    ):
        async with self.session_pool() as session:
            repo = RequestsRepo(session)
            event_from_user = data.get("event_from_user")

            user = await repo.users_actions.create_tg_user(
                user_id=event_from_user.id,
                username=event_from_user.username,
                first_name=event_from_user.first_name,
                last_name=event_from_user.last_name,
                
            )

            data['repo'] = repo
            data['user'] = user

            result = await handler(event, data)
        return result
