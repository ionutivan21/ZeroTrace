# conftest for tests - minimal
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from backend.app.database import Base

@pytest.fixture(scope='session')
def event_loop():
    import asyncio
    loop = asyncio.get_event_loop()
    yield loop
