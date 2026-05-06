"""
Test for Update User.
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.objects.users_object import Users
from utils.logger import get_logger

logger = get_logger(__name__)


def test_update_user():
    """Test updating a user."""
    users_api = Users()
    
    name = "John Brown"
    logger.info("Get user details")
    response = users_api.get_users({name: name})
    data = response.json()
    user_id = data[0]["id"]
    
    payload = {
        "email": "john_brown01@dummy.test",
        "status": "inactive"
    }
    
    logger.info("Updating a user")
    response = users_api.update_user(user_id, payload)
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    data = response.json()
    assert isinstance(data, dict), "Response should be a dict"
    assert "id" in data, "Invalid data"
    
    logger.info(f"Successfully updated user: {data}")
    