from sqlalchemy import BIGINT, String
from sqlalchemy.orm import mapped_column, Mapped

from database.models.base import Base


class TgUser(Base):
    __tablename__ = "tg_users"

    user_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=False)
    username: Mapped[str] = mapped_column(String(32))
    first_name: Mapped[str] = mapped_column(String(64), nullable=False)
    last_name: Mapped[str] = mapped_column(String(64), nullable=True)
