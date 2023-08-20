
from loguru import logger
import gc

class cache:

    @staticmethod
    def clear():
        
        def decorator(func):

            def wrapper(*args, **kwargs):
                
                result =  func(*args, **kwargs)
                gc.collect()
                return result
                
            return wrapper
        
        return decorator
    
    # @staticmethod
    # def clear_pytorch():
        
    #     def decorator(func):

    #         def wrapper(*args, **kwargs):
                
    #             result =  func(*args, **kwargs)
    #             torch.cuda.empty_cache()
    #             return result
                
    #         return wrapper
        
    #     return decorator