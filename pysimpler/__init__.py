from .errors import error
from .timers import timer
from .caches import cache
from .constants import MLFrameworks
from .report import reporter

# Format log messages
import sys
from loguru import logger
format = " <green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <red>PYSIMPLER </red> | <level>{level: <4}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"
logger.remove()  # All configured handlers are removed
logger.add(sys.stderr, format=format)