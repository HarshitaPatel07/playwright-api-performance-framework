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
    response = users_api.create_user(create_user_payload())
    user = response.json()

    yield user


class TestDeleteUserPositive:
    def test_delete_user(self, user_to_delete):
        response = users_api.delete_user(user_to_delete["id"])
        assert_status_code(response, 204)

    def test_get_deleted_user(self, user_to_delete):
        response = users_api.get_user_by_id(user_to_delete["id"])
        assert_status_code(response, 404)


class TestDeleteUserNegative:

    def test_delete_deleted_user(self, user_to_delete):
        response = users_api.delete_user(user_to_delete["id"])
        assert_status_code(response, 404)

    @pytest.mark.parametrize("user_id", [999999999, "abc"])
    def test_delete_invalid_user_id(self, user_id):
        response = users_api.delete_user(user_id)
        assert_status_code(response, 404)
