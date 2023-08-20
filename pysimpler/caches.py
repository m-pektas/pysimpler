
from loguru import logger
import gc
from .constants import ML_FRAMEWORKS


class cache:

    @staticmethod
    def clear(ml_framework : ML_FRAMEWORKS = ML_FRAMEWORKS.default):
        
        def decorator(func):

            def wrapper(*args, **kwargs):
                result =  func(*args, **kwargs)
                gc.collect()
                if ml_framework == ML_FRAMEWORKS.pytorch:
                    import torch
                    torch.cuda.empty_cache() 

                return result
                
            return wrapper
        
        return decorator
    
