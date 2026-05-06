"""
Test for Create User.
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.objects.users_object import Users
from utils.logger import get_logger

logger = get_logger(__name__)


def test_create_user():
    """Test creating a user."""
    users_api = Users()
    
    payload = {
        "name": "John Brown",
        "email": "johnbrown@dummy.test",
        "gender": "male",
        "status": "active"
    }
    
    logger.info("Creating a user")
    response = users_api.create_user(payload)
    
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    
    data = response.json()
    assert isinstance(data, dict), "Response should be a dict"
    assert "id" in data, "Invalid data"
    
    logger.info(f"Successfully created user: {data}")
    