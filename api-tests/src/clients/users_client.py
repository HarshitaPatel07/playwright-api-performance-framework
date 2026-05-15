import requests
from typing import Optional


from .base_api import BaseAPI
from src.utils.logger import get_logger

logger = get_logger(__name__)


class UsersClient(BaseAPI):
    """Users API Object for managing user endpoints."""

    endpoint = "/users"

    def get_user(self, params: Optional[dict] = None) -> requests.Response:
        """
        Fetch all users from the API.

        Args:
            params: Optional query parameters

        Returns:
            requests.Response: API response object
        """
        return self.request("GET", self.endpoint, params=params)

    def get_user_by_id(
        self, user_id: int, params: Optional[dict] = None
    ) -> requests.Response:
        """
        Fetch a user by ID.

        Args:
            user_id: The user ID to fetch
            params: Optional query parameters

        Returns:
            requests.Response: API response object
        """
        return self.request("GET", f"{self.endpoint}/{user_id}", params=params)

    def create_user(self, payload: dict):
        """
        Create a user

        Args:
            payload: the payload to create user

        Returns:
            requests.Response: API response object
        """
        return self.request("POST", self.endpoint, json=payload)

    def partial_update_user(self, user_id: int, payload: dict):
        """
        Partially update a user by ID

        Args:
            user_id: The user ID to update
            payload: the payload to update user

        Returns:
            requests.Response: API response object
        """
        return self.request("PATCH", f"{self.endpoint}/{user_id}", json=payload)

    def update_user(self, user_id: int, payload: dict):
        """
        Update a user by ID

        Args:
            user_id: The user ID to update
            payload: the payload to update user

        Returns:
            requests.Response: API response object
        """
        return self.request("PUT", f"{self.endpoint}/{user_id}", json=payload)

    def delete_user(self, user_id: int):
        """
        Delete a user by ID

        Args:
            user_id: The user ID to delete

        Returns:
            requests.Response: API response object
        """
        return self.request("DELETE", f"{self.endpoint}/{user_id}")
