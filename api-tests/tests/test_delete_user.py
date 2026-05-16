"""
Test for Delete User.
"""

import pytest

from src.clients.users_client import UsersClient
from src.utils.logger import get_logger
from src.utils.assertions import *
from tests.data.test_data import create_user_payload

logger = get_logger(__name__)

users_api = UsersClient()


@pytest.fixture(scope="module")
def user_to_delete():
    """Create own user for DELETE tests"""
    payload = create_user_payload()
    logger.info(f"Fixture: creating user for DELETE tests: {payload}")
    response = users_api.create_user(payload)
    user = response.json()
    logger.info(f"Fixture: user created with id={user['id']}")

    yield user


class TestDeleteUserPositive:
    def test_delete_user(self, user_to_delete):
        logger.info(f"Deleting user id={user_to_delete['id']}")
        response = users_api.delete_user(user_to_delete["id"])
        assert_status_code(response, 204)
        logger.info(f"User id={user_to_delete['id']} deleted successfully")

    def test_get_deleted_user(self, user_to_delete):
        logger.info(
            f"Verifying deleted user id={user_to_delete['id']} is not accessible"
        )
        response = users_api.get_user_by_id(user_to_delete["id"])
        assert_status_code(response, 404)
        logger.info("Deleted user returns 404")


class TestDeleteUserNegative:

    def test_delete_deleted_user(self, user_to_delete):
        logger.info(
            f"Attempting to delete already deleted user id={user_to_delete['id']}"
        )
        response = users_api.delete_user(user_to_delete["id"])
        assert_status_code(response, 404)
        logger.info("Returned 404 for already deleted user ")

    @pytest.mark.parametrize("user_id", [999999999, "abc"])
    def test_delete_invalid_user_id(self, user_id):
        logger.info(f"Deleting user with invalid id={user_id}")
        response = users_api.delete_user(user_id)
        assert_status_code(response, 404)
        logger.info(f"Returned 404 for invalid id={user_id}")
