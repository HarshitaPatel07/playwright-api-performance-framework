import pytest
import logging
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from utils.logger import init_session_logger, get_logger

def pytest_configure(config):
    test_paths = config.args
    if test_paths:
        test_name = os.path.splitext(os.path.basename(test_paths[0]))[0]
    else:
        test_name = "api_test"

    init_session_logger(test_name)

    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)


@pytest.fixture(autouse=True)
def log_test_info(request):
    """Log test start and end information."""
    logger = get_logger(__name__)
    logger.info(f"Starting test: {request.node.name}")
    yield
    logger.info(f"Completed test: {request.node.name}")