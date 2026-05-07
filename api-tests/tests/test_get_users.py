"""
Test for Get all Users.
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.objects.users_object import Users
from utils.logger import get_logger

logger = get_logger(__name__)


def test_get_users():
    """Test fetching all users."""
    users_api = Users()
    
    logger.info("Fetching all users")
    response = users_api.get_users()
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    data = response.json()
    assert isinstance(data, list), "Response should be a list"
    
    logger.info(f"Successfully fetched {len(data)} users")
    