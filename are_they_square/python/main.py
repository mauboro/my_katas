from math import sqrt

def is_square(arr):
    def is_square(n):
        return sqrt(n) ==  int(sqrt(n))
    return all([is_square(n) for n in arr]) if arr else None
