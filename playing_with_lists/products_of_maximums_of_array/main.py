from math import prod

def max_product(lst, n):
    return prod(sorted(lst)[-n:])

