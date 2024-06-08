from sqlalchemy.dialects.sqlite import insert

from database.models.users import TgUser
from database.repo.base import BaseRepo


class UserRepo(BaseRepo):
    async def create_tg_user(
            self,
            user_id: int,
            username: int | None,
            first_name: str,
            last_name: str | None,
    ):

        insert_query = (
            insert(TgUser)
            .values(
                user_id=user_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
            )
            .on_conflict_do_update(
                index_elements=[TgUser.user_id],
                set_=dict(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                ),
            )
            .returning(TgUser)
        )

        result = await self.session.execute(insert_query)

        await self.session.commit()
        return result.scalar_one()
