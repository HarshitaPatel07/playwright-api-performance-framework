"""
Base API class with common functionality.
"""
import requests
from typing import Optional, Dict
from abc import ABC

from config import BASE_URL, ACCESS_TOKEN
from src.utils.logger import get_logger

logger = get_logger(__name__)


class BaseAPI(ABC):
    """Base class for all API objects."""
    
    def __init__(self, endpoint: str):
        self.base_url = BASE_URL
        self.access_token = f'Bearer {ACCESS_TOKEN}' if ACCESS_TOKEN else None
        self.endpoint = endpoint
        logger.debug(f"{self.__class__.__name__} initialized with endpoint: {endpoint}")

    def _get_headers(self, extra_headers: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        """Get default headers with optional extras."""
        headers = {"Content-Type": "application/json"}
        if self.access_token:
            headers["Authorization"] = self.access_token
        if extra_headers:
            headers.update(extra_headers)
        return headers

    def _make_request(self, method: str, url: str, **kwargs) -> requests.Response:
        """Make HTTP request with logging and error handling."""
        
        try:
            logger.debug(f"Making {method} request to {url}")
            response = requests.request(method, url, **kwargs)
            
            logger.info(f"{method} {url} - Status: {response.status_code}")
            return response
        except requests.RequestException as err:
            logger.error(f"Request failed: {err}")
            raise
