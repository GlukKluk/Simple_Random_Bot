from sqlalchemy import BIGINT, String, Boolean
from sqlalchemy.orm import mapped_column, Mapped

from database.models.base import Base


class TgUser(Base):
    __tablename__ = "tg_users"

    user_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=False)
    username: Mapped[str] = mapped_column(String(32), nullable=True)
    first_name: Mapped[str] = mapped_column(String(64), nullable=False)
    last_name: Mapped[str] = mapped_column(String(64), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
