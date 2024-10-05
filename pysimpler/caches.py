"""Caches module"""
import os
import gc
from .enums import MLFrameworks


class Cache:
    """Cache class"""

    @staticmethod
    def clear(ml_framework: MLFrameworks = MLFrameworks.DEFAULT):
        def decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                if os.getenv("PYSIMPLER") == "1":
                    gc.collect()
                    if ml_framework == MLFrameworks.PYTORCH:
                        import torch

                        torch.cuda.empty_cache()
                    elif ml_framework == MLFrameworks.TENSORFLOW:
                        import tensorflow as tf

                        tf.keras.backend.clear_session()
                    elif ml_framework == MLFrameworks.KERAS:
                        import keras.backend as K

                        K.clear_session()

                return result

            return wrapper

        return decorator
