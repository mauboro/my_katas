from math import sqrt

def is_square(n):    
    if n < 0:
        return False
    else:
        return sqrt(n).is_integer()
