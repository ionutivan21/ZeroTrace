import pytest
import asyncio
from httpx import AsyncClient
from backend.app.main import app
from backend.app.database import Base, engine

@pytest.fixture(scope='session')
async def async_client():
    async with AsyncClient(app=app, base_url='http://testserver') as ac:
        yield ac

@pytest.mark.asyncio
async def test_root(async_client):
    r = await async_client.get('/')
    assert r.status_code == 200
    assert r.json().get('message')
