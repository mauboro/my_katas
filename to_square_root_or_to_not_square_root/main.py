from math import sqrt

def int_root(n):
    return sqrt(n) == int(sqrt(n))

def square_or_square_root(arr):
    return [sqrt(n) if int_root(n) else n**2 for n in arr]
