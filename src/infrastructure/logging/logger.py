from loguru import logger

logger.add(
    "logs/app.log",
    rotation="100 MB",
    retention="30 days",
    enqueue=True
)

logger.add(
    "logs/error.log",
    level="ERROR",
    rotation="100 MB"
)