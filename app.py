"""
PYSIMPLER example usage script.
"""

import torch
from loguru import logger
import pysimpler


@pysimpler.error.catch(raise_exception=False)
def zero_devision(x):
    """Zero devision error example function"""
    return x / 0


@pysimpler.timer.actual()
def counter_short(count):
    """Counter example function"""
    x = 1
    for i in range(count):
        x * i


@pysimpler.timer.actual()
def counter_long(count):
    """CounterLong example function"""
    logger.error("counterLong")
    x = 1
    for i in range(count):
        x * i


@pysimpler.cache.clear()
def memory(count):
    """Memory example function"""
    mem = []
    for _ in range(count):
        mem.append("data")


@pysimpler.cache.clear(pysimpler.MLFrameworks.PYTORCH)
def memory_pytorch(device="mps"):
    """Memory with a ML framework example function"""
    var = torch.ones(1, 3, 1024, 1024)
    if torch.cuda.is_available():
        var = var.to(device)


if __name__ == "__main__":
    print("Process 1")
    print("Process 2")
    result = memory_pytorch(device="cuda:0")
    result = memory(10000)
    result = counter_short(100)
    result = counter_long(1000)
    result = zero_devision(x=10)
    print("Process 4")
    pysimpler.reporter.report()
