
from loguru import logger
import traceback
import os

class error:

    @staticmethod
    def catch(raise_exception=True):
        
        def decorator(func):
            def wrapper(*args, **kwargs):

                if os.getenv("PYSIMPLER") == "1":
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        message =  "".join(traceback.format_exc().split("File")[2:]).replace("\n","")
                        logger.error(message) 

                        if raise_exception: raise e
                else:
                    return func(*args, **kwargs)

                
            return wrapper
        
        return decorator