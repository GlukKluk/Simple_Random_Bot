from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from database.models.base import Base


def create_db_engine(echo=False):
    engine = create_async_engine(
        url="sqlite+aiosqlite:///database.db",
        echo=echo
    )
    return engine


def create_session_pool(engine):
    return async_sessionmaker(bind=engine)


async def init_models(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
