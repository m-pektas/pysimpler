"""Error handling module"""
import os
import traceback
from .logger import pysimpler_logger


class Error:
    """Error handling class"""

    @staticmethod
    def catch(raise_exception=True):
        """Error handling function"""

        def decorator(func):
            def wrapper(*args, **kwargs):
                if os.getenv("PYSIMPLER") == "1":
                    try:
                        return func(*args, **kwargs)
                    except Exception as e:
                        message = "".join(
                            traceback.format_exc().split("File")[2:]
                        ).replace("\n", "")
                        pysimpler_logger.error(message)

                        if raise_exception:
                            raise e
                else:
                    return func(*args, **kwargs)

            return wrapper

        return decorator
