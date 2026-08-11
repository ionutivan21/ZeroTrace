import asyncio
import os
from getpass import getpass
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.database import async_session
from backend.app.auth.crud import create_user

async def seed_founder():
    username = input('Founder username [TinKode]: ') or 'TinKode'
    email = input('Founder email [securitatecibernetica5@gmail.com]: ') or 'securitatecibernetica5@gmail.com'
    password = getpass('Founder password (will not be shown): ')
    if not password:
        print('Password is required')
        return
    async with async_session() as db:
        # create founder user
        user = await create_user(db, username=username, email=email, password=password, role='FOUNDER')
        print('Founder created with id:', user.id)

if __name__ == '__main__':
    asyncio.run(seed_founder())
