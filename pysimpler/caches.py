
from loguru import logger
import gc
from .constants import MLFrameworks


class cache:

    @staticmethod
    def clear(ml_framework : MLFrameworks = MLFrameworks.DEFAULT):
        
        def decorator(func):

            def wrapper(*args, **kwargs):
                result =  func(*args, **kwargs)
                gc.collect()
                if ml_framework == MLFrameworks.PYTORCH:
                    import torch
                    torch.cuda.empty_cache() 

                return result
                
            return wrapper
        
        return decorator
    
