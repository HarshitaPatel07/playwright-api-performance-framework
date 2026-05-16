"""
Test for Update User.
"""

import pytest

from src.clients.users_client import UsersClient
from src.utils.logger import get_logger
from src.utils.assertions import *
from tests.data.test_data import (
    create_user_payload,
    update_user_payload,
    UPDATE_USER_NAME,
    UPDATE_USER_EMAIL,
    UPDATE_USER_INVALID_EMAIL,
)

logger = get_logger(__name__)

users_api = UsersClient()


@pytest.fixture(scope="module")
def user_to_update():
    """Create own user for Update tests"""
    logger.info("Fixture: creating users for UPDATE tests")
    response = users_api.create_user(create_user_payload())
    user1 = response.json()
    logger.info(f"Fixture: user1 created with id={user1['id']}")

    response = users_api.create_user(create_user_payload("Mark Fox"))
    user2 = response.json()
    logger.info(f"Fixture: user2 created with id={user2['id']}")

    response = users_api.create_user(create_user_payload("Patch Test User"))
    user3 = response.json()
    logger.info(f"Fixture: user3 created with id={user3['id']}")

    yield {"user1": user1, "user2": user2, "user3": user3}

    for user in [user1, user2, user3]:
        logger.info(f"Fixture teardown: deleting user id={user['id']}")
        users_api.delete_user(user["id"])  # delete user after test completes


class TestUpdateUserPositive:
    def test_update_user_name(self, user_to_update):
        user_id = user_to_update["user1"]["id"]
        logger.info(f"PATCH name for user id={user_id}, payload: {UPDATE_USER_NAME}")
        response = users_api.partial_update_user(user_id, UPDATE_USER_NAME)
        assert_status_code(response, 200)
        assert_fields_match(response.json(), UPDATE_USER_NAME, ["name"])
        logger.info(f"Name updated successfully for user id={user_id}")

    def test_update_user_email(self, user_to_update):
        user_id = user_to_update["user1"]["id"]
        logger.info(f"PATCH email for user id={user_id}, payload: {UPDATE_USER_EMAIL}")
        response = users_api.partial_update_user(user_id, UPDATE_USER_EMAIL)
        assert_status_code(response, 200)
        assert_fields_match(response.json(), UPDATE_USER_EMAIL, ["email"])
        logger.info(f"Email updated successfully for user id={user_id}")

    def test_update_user(self, user_to_update):
        user_id = user_to_update["user1"]["id"]
        payload = update_user_payload()
        logger.info(f"Updating details of user id = {user_id}, payload: {payload}")
        response = users_api.update_user(user_id, payload)
        assert_status_code(response, 200)

        data = response.json()

        assert_fields_match(data, payload, ["name", "email", "gender", "status"])
        logger.info("All details successfully updated")

    def test_patch_does_not_affect_other_fields(self, user_to_update):
        """Verify PATCH only changes targeted field, rest unchanged"""
        user3 = user_to_update["user3"]
        logger.info(f"Verifying PATCH field isolation for user id={user3['id']}")

        response = users_api.partial_update_user(user3["id"], UPDATE_USER_NAME)
        assert_status_code(response, 200)
        assert_fields_unchanged(response.json(), user3, exclude_fields=["name"])
        logger.info("No other fields changed verified")


class TestUpdateUserNegative:
    @pytest.mark.parametrize("user_id", [999999999, "abc", -1, 0])
    def test_update_invalid_user_id(self, user_id):
        logger.info(f"Updating user with invalid id={user_id}")
        response = users_api.update_user(user_id, update_user_payload())
        assert_status_code(response, 404)
        logger.info(f"Returned 404 for invalid id={user_id}")

    def test_update_invalid_email(self, user_to_update):
        user_id = user_to_update["user1"]["id"]
        logger.info(f"Updating user id={user_id} with invalid email")
        response = users_api.partial_update_user(user_id, UPDATE_USER_INVALID_EMAIL)
        assert_status_code(response, 422)
        logger.info("Invalid email not updated with status 422")

    def test_update_duplicate_email(self, user_to_update):
        user1 = user_to_update["user1"]
        user2 = user_to_update["user2"]
        payload = {"email": user2["email"]}
        logger.info(
            f"Updating user id={user1['id']} with duplicate email={user2['email']}"
        )

        response = users_api.partial_update_user(user1["id"], payload)
        assert_status_code(response, 422)
        logger.info("Duplicate email not updated with status 422")
