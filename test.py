from deco import *


# 1 1 2 3 5 8 13 21 34 55
@count_sec
def fib(n):
    if n in [1, 2]:
        return 1
    return (fib(n-1) + fib(n-2))


@count_sec
def fib1(n):
    start = 1
    next = 1
    for i in range(n-1):
        temp = start
        start += next
        next = temp
    return next


# print(fib(20))
# print(fib1(20))
print('test.py')