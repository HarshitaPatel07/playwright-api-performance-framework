"""
Test data for API tests.
"""
import json
from typing import Dict, Any


# User test data
USER_DATA = {
    "valid_user": {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "gender": "male",
        "status": "active"
    },
    "update_user": {
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "gender": "female",
        "status": "inactive"
    },
    "invalid_user": {
        "name": "",  # Invalid: empty name
        "email": "invalid-email",  # Invalid: bad email format
        "gender": "other",
        "status": "pending"
    }
}


def get_test_user(user_type: str = "valid_user") -> Dict[str, Any]:
    """Get test user data by type."""
    return USER_DATA.get(user_type, USER_DATA["valid_user"]).copy()
