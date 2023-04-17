from functools import partial 
from inspect import signature

arr = [1, 2, 3]
integer = 2

def multiply_all_test(arr: list, integer: int):
    arr = arr[:]
    return [n * integer for n in arr]

take_arr = partial(multiply_all_test, arr)
do_it = partial(take_arr, 3)

print(do_it())

from functools import partial 

def curry(fnc):
    def inner(arg):
        if len(signature(fnc).parameters) == 1:
            return fnc(arg)
        
        return curry(partial(fnc, arg))
    
    return inner

@curry
def multiply_all(arr, integer):
    return [n * integer for n in arr]


def multiply_all_refactored(arr):
    def m(n):
        return [i * n for i in arr]
    return m
