from typing import Generator

import httpx
import pytest
from fastapi.testclient import TestClient

from main import app

# this is a comment
# this is another comment

@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)


def test_health_check(client: TestClient):
    res: httpx.Response = client.get("/health_check")
    assert res.status_code == 200
    assert res.json() == {"status":"ok"}


def test_request_countet(client: TestClient):
    res: httpx.Response = client.get("/total_requests")
    assert res.status_code == 200
    assert res.json() == {"total_reqeusts":1}

    res: httpx.Response = client.get("/total_requests")
    assert res.status_code == 200
    assert res.json() == {"total_reqeusts":2}

