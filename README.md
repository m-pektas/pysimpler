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
```
# output
------------------------------
Process 1
Process 2
Process 3
func : zero devision => 10/0
2023-08-20T03:11:50.412347+0300 | ERROR |  "/Users/mp/Desktop/Github/simpler/app.py", line 8, in zero_devision
    return x/0
ZeroDivisionError: division by zero

Process 4
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
```
# output
------------------------------
Process 1
Process 2
Process 3
2023-08-20T03:13:23.631413+0300 | INFO | Function : counter | Duration : 0.0003120899200439453 sec
Process 4
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
    # print(gc.get_count()) lines are only for printing of the memory state. 
    # You can remove it.

    print("Process 1")
    print("Process 2")
    print(gc.get_count()) 
    result = memory(1000)
    print(gc.get_count())
    print("Process 4")

```
```
# output
------------------------------
Process 1
Process 2
Process 3
(351, 10, 1)
(0, 0, 0)
Process 4
```