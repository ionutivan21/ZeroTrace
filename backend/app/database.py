from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import event

from .config import settings

engine = create_async_engine(settings.DATABASE_URL, future=True, echo=False)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

# convenience sync engine for creating tables in startup
sync_engine = engine.sync_engine
