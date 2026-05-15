"""
Test for Create User.
"""

import pytest

from src.clients.users_client import UsersClient
from src.utils.logger import get_logger
from tests.data.test_data import create_user_payload, CREATE_USER_INVALID_CASES

logger = get_logger(__name__)
users_api = UsersClient()


@pytest.fixture()
def cleanup_user():
    """Tracks and deletes users created inside create tests"""
    created_ids = []
    yield created_ids
    for user_id in created_ids:
        users_api.delete_user(user_id)


class TestCreateUserPositive:
    def test_create_valid_user(self, cleanup_user):
        payload = create_user_payload()
        response = users_api.create_user(payload)
        assert response.status_code == 201

        data = response.json()
        cleanup_user.append(data["id"])

        assert "id" in data, "Response should contain id"
        assert data["name"] == payload["name"]
        assert data["email"] == payload["email"]
        assert data["gender"] == payload["gender"]
        assert data["status"] == payload["status"]


class TestCreateUserNegative:

    @pytest.mark.parametrize("payload, expected_status", CREATE_USER_INVALID_CASES)
    def test_create_invalid_payloads(self, payload, expected_status):
        response = users_api.create_user(payload)
        assert response.status_code == expected_status
