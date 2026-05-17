import logging
import os
from datetime import datetime

# path to the logs/ dir
LOGS_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

_CURRENT_TEST_LOG_FILE = None
_FILE_HANDLER_NAME = "current_test_file_handler"


def _get_root_file_handler():
    root_logger = logging.getLogger()
    for handler in list(root_logger.handlers):
        if getattr(handler, "name", None) == _FILE_HANDLER_NAME:
            return handler
    return None


def set_test_log_file(test_name: str):
    """Configure the root logger to write to a per-test-module file."""
    global _CURRENT_TEST_LOG_FILE

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    _CURRENT_TEST_LOG_FILE = os.path.join(LOGS_DIR, f"{test_name}_{timestamp}.log")

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    existing_handler = _get_root_file_handler()
    if existing_handler is not None:
        root_logger.removeHandler(existing_handler)
        existing_handler.close()

    file_handler = logging.FileHandler(_CURRENT_TEST_LOG_FILE)
    file_handler.name = _FILE_HANDLER_NAME
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT))
    root_logger.addHandler(file_handler)


def clear_test_log_file():
    """Remove the per-test-module file handler from the root logger."""
    global _CURRENT_TEST_LOG_FILE

    root_logger = logging.getLogger()
    existing_handler = _get_root_file_handler()
    if existing_handler is not None:
        root_logger.removeHandler(existing_handler)
        existing_handler.close()

    _CURRENT_TEST_LOG_FILE = None


def get_logger(name: str, log_level: str = "INFO") -> logging.Logger:
    """
    Get a configured logger instance.
    All loggers in the session write to the same file set by init_session_logger.
    
    Args:
        name: Logger name ( __name__)
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)

    # Avoid adding duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(getattr(logging, log_level))

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, log_level))
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT))

    logger.addHandler(console_handler)
    logger.propagate = True

    return logger