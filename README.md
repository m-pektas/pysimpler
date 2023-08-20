# pysimpler
This package simplifies the fundamental software engineering practices such as exception handling, logging etc.





### Try-Catch 

```python
import pysimpler

@pysimpler.error.catch(raise_exception=False)
def zero_devision(x):
    print(f"func : zero devision => {x}/0")
    return x/0

if __name__ == '__main__':
    print("Process 1")
    print("Process 2")
    result = zero_devision(x = 10)
    print("Process 4")
```


### Timer

```python
import pysimpler

@pysimpler.timer.actual()
def counter(count):
    x = 1
    for i in range(count):
        y = x*i

if __name__ == '__main__':

    print("Process 1")
    print("Process 2")
    result = counter(10)
    print("Process 4")
```



### Cache

```python
import pysimpler
import gc

@pysimpler.cache.clear()
def memory(count):
    mem = []
    for i in range(count):
        mem.append("data")

if __name__ == '__main__':
    print("Process 1")
    print("Process 2")
    print(gc.get_count())
    result = memory(1000)
    print(gc.get_count())
    print("Process 4")

