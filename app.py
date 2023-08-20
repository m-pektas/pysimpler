import pysimpler
import gc


@pysimpler.error.catch(raise_exception=False)
def zero_devision(x):
    print(f"func : zero devision => {x}/0")
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


if __name__ == '__main__':

    result = zero_devision(x = 10)
    result = counter(1000)
    result = memory(1000)
    print( "other processes" )
