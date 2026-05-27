"""
AXIOS OS Logger

Centralized structured logging system.
"""

import sys
from loguru import logger

from src.config.settings import Settings

# --------------------------------------------------
# Load Settings
# --------------------------------------------------

settings = Settings()

# --------------------------------------------------
# Logger Configuration
# --------------------------------------------------

LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "<level>{message}</level>"
)

# --------------------------------------------------
# Setup Logger
# --------------------------------------------------

def setup_logger():
    """
    Configure and return AXIOS OS logger.
    """

    # Remove default logger
    logger.remove()

    # Console Logger
    logger.add(
        sys.stdout,
        format=LOG_FORMAT,
        level=settings.LOG_LEVEL,
        colorize=True,
        enqueue=True,
        backtrace=True,
        diagnose=True,
    )

    # File Logger
    logger.add(
        f"{settings.LOG_PATH}/axios_os.log",
        rotation="10 MB",
        retention="10 days",
        compression="zip",
        format=LOG_FORMAT,
        level=settings.LOG_LEVEL,
        enqueue=True,
    )

    logger.info("Logger initialized.")

    return logger
