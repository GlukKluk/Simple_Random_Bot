from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from database.models.base import Base


def create_db_engine(echo=False):
    engine = create_async_engine(
        url="sqlite:///bot.db",
        echo=echo
    )
    return engine


def create_session_pool(engine):
    return async_sessionmaker(bind=engine)


def create_tables(engine):
    Base.metadata.create_all(bind=engine)