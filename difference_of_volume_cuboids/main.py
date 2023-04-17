import math
from functools import reduce

def find_difference(a, b):
    return abs(math.prod(a) - math.prod(b))

def find_difference_refactored(a, b):
    return abs(reduce(lambda x, y: x * y, a) - reduce(lambda x, y: x * y, a))

