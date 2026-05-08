import logging
import os
from datetime import datetime

# path to the logs/ dir
LOGS_DIR = os.path.join(os.path.dirname(__file__), '..', '..', 'logs')
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

_SESSION_LOG_FILE = None


def init_session_logger(test_name: str):
    """
    This gets called once at session start (from conftest.pytest_configure)
    to lock in the log file name before any logger is created.
    
    Args:
        test_name: The test file name without extension e.g. 'test_get_users'
    """
    global _SESSION_LOG_FILE
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    _SESSION_LOG_FILE = os.path.join(LOGS_DIR, f"{test_name}_{timestamp}.log")


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
    global _SESSION_LOG_FILE

    # Fallback if init_session_logger was never called (e.g. running a script directly)
    if _SESSION_LOG_FILE is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        _SESSION_LOG_FILE = os.path.join(LOGS_DIR, f"api_test_{timestamp}.log")

    logger = logging.getLogger(name)

    # Avoid adding duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(getattr(logging, log_level))

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, log_level))
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT))

    # File handler — always uses the session file
    file_handler = logging.FileHandler(_SESSION_LOG_FILE)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT))

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger