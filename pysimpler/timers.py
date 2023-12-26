
from loguru import logger
import sys
logger.remove(0)
logger.add(sys.stderr, format="{time} | {level} | {message}")
import time
import os
import inspect
from pysimpler.report import reporter

class timer:

    def ___get_func_info__(func):
        file_path = inspect.getsourcefile(func) # get filepaht
        name = func.__name__ # get func name
        return file_path, name


    @staticmethod
    def actual():
        
        def decorator(func):
            def wrapper(*args, **kwargs):

                if os.getenv("PYSIMPLER") == "1":
                    
                    function_file_path, function_name = timer.___get_func_info__(func)

                    s = time.perf_counter()
                    result = func(*args, **kwargs)
                    e = time.perf_counter()
                    logger.info(f"File: {function_file_path} | Function : {function_name} | Duration : {e-s} sec")
                    
                    key = function_file_path.split(".")[0]+"_"+function_name
                    val = e-s
                    reporter.add(key, val)
                else:
                    result = func(*args, **kwargs)
                return result
            return wrapper
        
        return decorator