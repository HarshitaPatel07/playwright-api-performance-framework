"""
Test for Delete User.
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.objects.users_object import Users
from utils.logger import get_logger

logger = get_logger(__name__)


def test_delete_user():
    """Test deleting a user."""
    users_api = Users()
    
    name = "John Brown"
    logger.info("Get user details")
    response = users_api.get_users({name: name})
    data = response.json()
    user_id = data[0]["id"]
    
    logger.info("Deleting a user")
    response = users_api.delete_user(user_id)
    
    assert response.status_code == 204, f"Expected 204, got {response.status_code}"
    
    logger.info("Successfully deleted user")
    