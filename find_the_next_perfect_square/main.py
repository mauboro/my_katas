from math import sqrt

def find_next_square(sq):
    if int(sqrt(sq)) == sqrt(sq):
        for n in range(sq+1, sq+1000000):
            if int(sqrt(n)) == sqrt(n):
                return n 
    else: 
        return -1

def find_next_square_refactored(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root+1) ** 2
    return -1

