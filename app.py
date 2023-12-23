import pysimpler
import gc
import torch


@pysimpler.error.catch(raise_exception=False)
def zero_devision(x):
    return x/0

@pysimpler.timer.actual()
def counter(count):
    x = 1
    for i in range(count):
        y = x*i

@pysimpler.cache.clear()
def memory(count):
    mem = []
    for i in range(count):
        mem.append("data")


@pysimpler.cache.clear(pysimpler.MLFrameworks.PYTORCH)
def memory_pytorch(device = "mps"):
    var = torch.ones(1,3,1024,1024)
    if torch.cuda.is_available():
        var = var.to(device)


if __name__ == '__main__':

    print("Process 1")
    print("Process 2")
    result = memory_pytorch(device="cuda:0")
    result = memory(10000)
    result = counter(10000)
    result = zero_devision(x = 10)
    print("Process 4")

    




    