import asyncio
from typing import Generator, Iterator

import pytest
from tortoise.contrib.test import finalizer, initializer
from fastapi.testclient import TestClient

from ..api import app


@pytest.fixture(scope='module')
def client() -> Generator:
    initializer(['models'])
    with TestClient(app) as c:
        yield c
    finalizer()


# @pytest.fixture(scope="module")
# def event_loop(client: TestClient) -> Generator:
#     yield client.task.get_loop()  # type: ignore

@pytest.fixture(scope="module")
def event_loop() -> Iterator[asyncio.AbstractEventLoop]:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    # loop.close()
