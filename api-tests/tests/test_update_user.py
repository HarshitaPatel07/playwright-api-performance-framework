"""
Test for Update User.
"""
from src.clients.users_client import UsersClient
from src.utils.logger import get_logger

logger = get_logger(__name__)


def test_update_user():
    """Test updating a user."""
    users_api = UsersClient()
    
    name = "John Brown"
    logger.info("Get user details")
    response = users_api.get_user({name: name})
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
    