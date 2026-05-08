"""
Test for Delete User.
"""
from src.clients.users_client import UsersClient
from src.utils.logger import get_logger

logger = get_logger(__name__)


def test_delete_user():
    """Test deleting a user."""
    users_api = UsersClient()
    
    name = "John Brown"
    logger.info("Get user details")
    response = users_api.get_users({name: name})
    data = response.json()
    user_id = data[0]["id"]
    
    logger.info("Deleting a user")
    response = users_api.delete_user(user_id)
    
    assert response.status_code == 204, f"Expected 204, got {response.status_code}"
    
    logger.info("Successfully deleted user")
    