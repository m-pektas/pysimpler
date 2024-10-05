"""
PYSIMPLER example usage script.
"""

import torch
import pysimpler
import time

# If you want to set specific values for timer as globally, you can use following lines. Default values are TIME_UNITS.SECONDS and 5 digits.
pysimpler.timer.set_time_unit(pysimpler.TIME_UNITS.SECONDS)
pysimpler.timer.set_digits(10)

# If you want to set specific values for reporter as globally, you can use following lines. Default values are TIME_UNITS.SECONDS and 5 digits.
pysimpler.reporter.set_time_unit(pysimpler.TIME_UNITS.MILLISECONDS)
pysimpler.reporter.set_digits(10)


@pysimpler.timer.time()
def counter_short(count):
    """Counter example function"""
    x = 1
    for i in range(count):
        x * i


@pysimpler.timer.time(
    time_unit=pysimpler.TIME_UNITS.MILLISECONDS
)  # If you want you can set different time unit or digit for each function.
def counter_shortest(count):
    """Counter example function"""
    x = 1
    for i in range(count):
        x * i


@pysimpler.timer.time()
def counter_long(count):
    """CounterLong example function"""
    x = 1
    for i in range(count):
        x * i


@pysimpler.timer.time()
def sleepy(count):
    """CounterLong example function"""
    time.sleep(count)


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
    memory_pytorch(device="cuda:0")
    memory(10000)
    counter_shortest(100)
    counter_short(100000)
    counter_long(1000000)
    sleepy(1)
    print("Process N")
    pysimpler.reporter.report()
