"""
Test for Get all Users.
"""
from src.clients.users_client import UsersClient
from src.utils.logger import get_logger

logger = get_logger(__name__)


def test_get_users():
    """Test fetching all users."""
    users_api = UsersClient()
    
    logger.info("Fetching all users")
    response = users_api.get_user()
    
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    data = response.json()
    assert isinstance(data, list), "Response should be a list"
    
    logger.info(f"Successfully fetched {len(data)} users")
    