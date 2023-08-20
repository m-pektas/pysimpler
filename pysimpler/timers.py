
from loguru import logger
import sys
logger.remove(0)
logger.add(sys.stderr, format="{time} | {level} | {message}")
from time import time

class timer:

    @staticmethod
    def actual():
        
        def decorator(func):
            def wrapper(*args, **kwargs):
                s = time()
                result = func(*args, **kwargs)
                e = time()
                logger.info(f"Function : {func.__name__} | Duration : {e-s} sec")
                return result
            return wrapper
        
        return decorator