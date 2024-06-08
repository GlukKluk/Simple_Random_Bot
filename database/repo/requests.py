from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession

from database.repo.users import UserRepo


@dataclass
class RequestRepo:

    session: AsyncSession

    @property
    def users_actions(self) -> UserRepo:
        return UserRepo(self.session)
