import requests
from typing import Optional


from .base_api import BaseAPI
from src.utils.logger import get_logger

logger = get_logger(__name__)


class UsersClient(BaseAPI):
    """Users API Object for managing user endpoints."""
    
    def __init__(self):
        self.endpoint = '/users'
        super().__init__(endpoint=self.endpoint)

    def get_user(self, params: Optional[dict] = None) -> requests.Response:
        """
        Fetch all users from the API.
        
        Args:
            params: Optional query parameters
            
        Returns:
            requests.Response: API response object
        """
        url = f"{self.base_url}{self.endpoint}"
        headers = self._get_headers()
        
        try:
            response = requests.get(url, params=params, headers=headers)
            logger.info(f"GET {url} - Status: {response.status_code}")
            return response
        except requests.RequestException as err:
            logger.error(f"Request failed: {err}")
            raise

    def get_user_by_id(self, user_id: int, params: Optional[dict] = None) -> requests.Response:
        """
        Fetch a user by ID.
        
        Args:
            user_id: The user ID to fetch
            params: Optional query parameters
            
        Returns:
            requests.Response: API response object
        """
        url = f"{self.base_url}{self.endpoint}/{user_id}"
        headers = self._get_headers()
        
        try:
            response = requests.get(url, params=params, headers=headers)
            logger.info(f"GET {url} - Status: {response.status_code}")
            return response
        except requests.RequestException as err:
            logger.error(f"Request failed for user_id {user_id}: {err}")
            raise

    def create_user(self, payload: dict):
        """
        Create a user
        
        Args:
            payload: the payload to create user
            
        Returns:
            requests.Response: API response object
        """
        url = f"{self.base_url}{self.endpoint}"
        headers = self._get_headers()
        
        try:
            response = requests.post(url, json=payload, headers=headers)
            logger.info(f"POST {url} - Status: {response.status_code}")
            return response
        except requests.RequestException as err:
            logger.error(f"Request failed: {err}")
            raise

    def update_user(self, user_id: int, payload: dict):
        """
        Update a user by ID
        
        Args:
            user_id: The user ID to update
            payload: the payload to update user
            
        Returns:
            requests.Response: API response object
        """
        url = f"{self.base_url}{self.endpoint}/{user_id}"
        headers = self._get_headers()
        
        try:
            response = requests.patch(url, json=payload, headers=headers)
            logger.info(f"PATCH {url} - Status: {response.status_code}")
            return response
        except requests.RequestException as err:
            logger.error(f"Request failed: {err}")
            raise

    def delete_user(self, user_id: int):
        """
        Delete a user by ID
        
        Args:
            user_id: The user ID to delete
            
        Returns:
            requests.Response: API response object
        """
        url = f"{self.base_url}{self.endpoint}/{user_id}"
        headers = self._get_headers()
        
        try:
            response = requests.delete(url, headers=headers)
            logger.info(f"DELETE {url} - Status: {response.status_code}")
            return response
        except requests.RequestException as err:
            logger.error(f"Request failed: {err}")
            raise