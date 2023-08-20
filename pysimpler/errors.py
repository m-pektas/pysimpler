
from loguru import logger
import traceback

class error:

    @staticmethod
    def catch(raise_exception=False):
        
        def decorator(func):
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    message =  "".join(traceback.format_exc().split("File")[2:])
                    logger.error(message) 

                    if raise_exception: raise e
                
            return wrapper
        
        return decorator