"""
Test for Get all Users.
"""

import pytest

from src.clients.users_client import UsersClient
from src.utils.logger import get_logger
from src.utils.assertions import *
from tests.data.test_data import create_user_payload

logger = get_logger(__name__)

users_api = UsersClient()


@pytest.fixture(scope="module")
def user_to_get():
    """Create own user for GET tests"""
    response = users_api.create_user(create_user_payload())
    user = response.json()

    yield user

    users_api.delete_user(user["id"])  # delete user after test completes


class TestGetUserPositive:
    def test_get_all_users(self):
        response = users_api.get_user()
        assert_status_code(response, 200)
        data = response.json()
        assert_response_is_list(response)

    def test_get_user_by_id(self, user_to_get):
        response = users_api.get_user_by_id(user_to_get["id"])
        assert_status_code(response, 200)

        data = response.json()

        assert_fields_match(
            data, user_to_get, ["id", "name", "email", "gender", "status"]
        )


class TestGetUserNegative:

    @pytest.mark.parametrize("user_id", [999999999, "abc", -1, 0])
    def test_get_invalid_user_id(self, user_id):
        response = users_api.get_user_by_id(user_id)
        assert_status_code(response, 404)
