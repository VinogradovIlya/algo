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

if __name__ == '__main__':
    create_string1()

    create_string2()
    print('deco.py')