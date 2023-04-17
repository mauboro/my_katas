import math
from functools import reduce

def grow(arr):
    return math.prod(arr)

def grow_refactored(arr):
    product = 1
    for i in arr:
        product *= i

    return product

def grow(arr):
    return reduce(lambda x, y: x*y, arr)
