import os
from time import *


def final_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(end - start)
        return res
    return wrapper


@final_time
def my_funk(a, b):
    print(a + b)


my_funk(10, 20)
# import time


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
