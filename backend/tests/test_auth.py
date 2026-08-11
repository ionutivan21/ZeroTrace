# Additional tests for critical flows
import pytest
from httpx import AsyncClient
from backend.app.main import app

@pytest.mark.asyncio
async def test_register_and_login():
    async with AsyncClient(app=app, base_url='http://testserver') as ac:
        r = await ac.post('/auth/register', json={'username':'testuser','email':'test@example.com','password':'testpass'})
        assert r.status_code == 200
        r2 = await ac.post('/auth/login', json={'username':'testuser','password':'testpass'})
        assert r2.status_code == 200
        assert 'access_token' in r2.json()
