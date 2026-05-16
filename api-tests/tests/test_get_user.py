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
    payload = create_user_payload()
    logger.info(f"Fixture: creating user for GET tests: {payload}")
    response = users_api.create_user(payload)
    user = response.json()
    logger.info(f"Fixture: user created with id={user['id']}")

    yield user

    logger.info(f"Fixture teardown: deleting user id={user['id']}")
    users_api.delete_user(user["id"])  # delete user after test completes


class TestGetUserPositive:
    def test_get_all_users(self):
        logger.info("Fetching all users")
        response = users_api.get_user()
        assert_status_code(response, 200)
        assert_response_is_list(response)
        logger.info("All assertions passed for get all users")

    def test_get_user_by_id(self, user_to_get):
        logger.info(f"Fetching user by id={user_to_get['id']}")
        response = users_api.get_user_by_id(user_to_get["id"])
        assert_status_code(response, 200)

        data = response.json()

        assert_fields_match(
            data, user_to_get, ["id", "name", "email", "gender", "status"]
        )
        logger.info(f"Correct user returned for id={user_to_get['id']}")


class TestGetUserNegative:

    @pytest.mark.parametrize("user_id", [999999999, "abc", -1, 0])
    def test_get_invalid_user_id(self, user_id):
        logger.info(f"Fetching user with invalid id={user_id}")
        response = users_api.get_user_by_id(user_id)
        assert_status_code(response, 404)
        logger.info(f"Correctly returned 404 for invalid id={user_id}")
