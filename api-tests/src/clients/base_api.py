"""
Base API class with common functionality.
"""

import requests
from typing import Optional, Dict
from abc import ABC, abstractmethod

from config import BASE_URL, ACCESS_TOKEN
from src.utils.logger import get_logger

logger = get_logger(__name__)


class BaseAPI(ABC):
    """Base class for all API objects."""

    def __init__(self):
        self.base_url = BASE_URL
        self.access_token = f"Bearer {ACCESS_TOKEN}" if ACCESS_TOKEN else None

    @property
    @abstractmethod
    def endpoint(self) -> str:
        """Every subclass must define its endpoint"""

    def _get_headers(
        self, extra_headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, str]:
        """Get default headers with optional extras."""
        headers = {"Content-Type": "application/json"}
        if self.access_token:
            headers["Authorization"] = self.access_token
        if extra_headers:
            headers.update(extra_headers)
        return headers

    def request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Make HTTP request with logging and error handling."""

        url = f"{self.base_url}{endpoint}"
        headers = self._get_headers(kwargs.pop("extra_headers", None))

        # if "json" in kwargs:
        #     logger.debug(f"Request Body: {kwargs['json']}")
        # if "params" in kwargs:
        #     logger.debug(f"Query Params: {kwargs['params']}")

        try:
            response = requests.request(
                method=method, url=url, headers=headers, **kwargs
            )
            logger.info(f"{method} {url} - Status: {response.status_code}")

            # logger.debug(f"Response Body: {response.json()}")
            return response

        except requests.RequestException as err:
            logger.error(f"{method} {url} failed: {err}")
            raise
