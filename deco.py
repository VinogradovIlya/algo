import time
import os
from time import *


def count_sec(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(end - start)
        return res
    return wrapper

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(
#             f"Время выполнения функции {func.__name__}: {end_time - start_time} сек.")
#         return result
#     return wrapper


# @timer
# def some_function():
#     time.sleep(2)


# some_function()

@count_sec
def create_string1():
    res = ''
    for i in range(1_000_000_00):
        res += str(i)
    return res


@count_sec
def create_string2():
    res = ''.join(list(map(str, [i for i in range(1_000_000_00)])))
    return res


create_string1()

create_string2()
