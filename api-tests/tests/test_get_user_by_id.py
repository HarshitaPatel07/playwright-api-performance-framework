"""
Test for Get User by id.
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.objects.users_object import Users
from utils.logger import get_logger

logger = get_logger(__name__)


def test_get_user():
    """Test fetching user by id"""
    users_api = Users()
    
    logger.info("Fetching user by id")
    
    user_id = 8458627
    response = users_api.get_user_by_id(user_id)
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    data = response.json()
    assert "id" in data, "Invalid data"
    
    logger.info(data)
    