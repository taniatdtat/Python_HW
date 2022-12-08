import time
from functools import lru_cache

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start_time)
        return res
    return wrapper

def fib_rec_f(n):
    if n == 0 :
        return 0
    elif n ==1:
        return 1
    else:
        return fib_rec_f(n - 1) + fib_rec_f(n - 2)

@time_decorator
def fib_rec(n):
    return fib_rec_f(n)


@lru_cache(maxsize=None)
def  fib_rec_Iru(n):
    return fib_rec_f(n)

@time_decorator
def FIB_rec_Iru(n):
    return fib_rec_Iru(n)

def fib_dyn_f(n):
    arr = [0,1] + [0]*(n-1)
    for i in range(2, n+1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]

@time_decorator
def fib_dyn(n):
    return fib_dyn_f(n)

@lru_cache(maxsize=None)
def  fib_dyn_Iru(n):
    return fib_dyn_f(n)

@time_decorator
def FIB_dyn_Iru(n):
    return fib_dyn_Iru(n)

print('c lru_cache')
print ('рекурсия ')
print(FIB_rec_Iru(4))
print ('циклы')
print(FIB_dyn_Iru(4))
print('без lru_cache')
print ('рекурсия ')
print(fib_dyn(4))
print ('рекурсия ')
print( fib_rec(4))
