import pytest
import logging
import os
import glob
import shutil
from pathlib import Path

from src.utils.logger import clear_test_log_file, get_logger, LOGS_DIR, set_test_log_file


def pytest_configure(config):
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    if os.path.exists(LOGS_DIR):
        # create a logs/backup dir if it doesn't exist
        logs_backup_dir = os.path.join(LOGS_DIR, "backup")
        os.makedirs(logs_backup_dir, exist_ok=True)

        # move all current .log files from logs/ to backup/
        log_files = glob.glob(os.path.join(LOGS_DIR, "*.log"))
        for log_file in log_files:
            shutil.move(log_file, logs_backup_dir)

        # from backup/ keep only last 10 .log files, delete the rest
        old_log_files = sorted(
            glob.glob(os.path.join(logs_backup_dir, "*.log")), key=os.path.getmtime
        )
        for log_file in old_log_files[:-10]:
            os.remove(log_file)


@pytest.fixture(scope="module", autouse=True)
def test_module_logger(request):
    """Use one log file per test module."""
    test_name = Path(str(request.node.fspath)).stem
    set_test_log_file(test_name)
    yield
    clear_test_log_file()


@pytest.fixture(autouse=True)
def log_test_info(request):
    """Log test start and end information."""
    logger = get_logger(__name__)
    logger.info(f"{'='*60}")
    logger.info(f"Starting test: {request.node.name}")
    yield
    logger.info(f"Completed test: {request.node.name}")
    logger.info(f"{'='*60}")
