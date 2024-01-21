"""Timer module"""
import os
import time
import inspect
from pysimpler.report import Reporter
from .logger import pysimpler_logger


class Timer:
    """Timer class"""

    def get_func_info(func):
        """This function gives information about the called function."""
        file_path = inspect.getsourcefile(func)  # get filepaht
        file_path = "/".join(file_path.split("/")[-2:])
        name = func.__name__  # get func name
        return file_path, name

    @staticmethod
    def actual():
        """This function logs duration information of the called function."""

        def decorator(func):
            def wrapper(*args, **kwargs):
                if os.getenv("PYSIMPLER") == "1":
                    function_file_path, function_name = Timer.get_func_info(func)

                    s = time.perf_counter()
                    result = func(*args, **kwargs)
                    e = time.perf_counter()
                    pysimpler_logger.info(
                        f"File: {function_file_path} | Function : {function_name} | Duration : {e-s} sec"
                    )

                    key = (
                        function_file_path.split("/")[-1].split(".")[0]
                        + "_"
                        + function_name
                    )
                    val = e - s
                    Reporter.add(key, val)
                else:
                    result = func(*args, **kwargs)
                return result

            return wrapper

        return decorator
