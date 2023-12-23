
import gc
from .constants import MLFrameworks
import os

class cache:

    @staticmethod
    def clear(ml_framework : MLFrameworks = MLFrameworks.DEFAULT):
        
        def decorator(func):

            def wrapper(*args, **kwargs):
                result =  func(*args, **kwargs)
                if os.getenv("PYSIMPLER") == "1":
                    gc.collect()
                    if ml_framework == MLFrameworks.PYTORCH:
                        import torch
                        torch.cuda.empty_cache() 

                return result
                
            return wrapper
        
        return decorator
    
