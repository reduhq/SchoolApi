from typing import AsyncGenerator

import pytest_asyncio

from httpx import AsyncClient

from sqlalchemy.ext.asyncio import AsyncSession

from schoolapi.core.config import settings
from schoolapi.db.session import AsyncSessionLocal
from schoolapi.main import app
from schoolapi.tests.utils.user import authentication_token_from_email
from schoolapi.tests.utils.utils import get_superuser_token_headers 


@pytest_asyncio.fixture()
async def tmp_db() -> AsyncGenerator:
    async with AsyncSessionLocal() as db:
        yield db

# @pytest.fixture(scope='module')
# async def client() -> AsyncGenerator:
#     async with AsyncClient(app) as c:
#         yield c

# @pytest.fixture(scope='module')
# async def superuser_token_headers(client:AsyncClient) -> dict[str,str]:
#     return await get_superuser_token_headers(client)

# @pytest.fixture(scope='module')
# def normal_user_token_headers(client:AsyncClient, db:AsyncSession) -> dict[str,str]:
#     return authentication_token_from_email(
#         client = client, email = settings.EMAIL_TEST_USER, db = db
#     )