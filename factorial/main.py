import math

def factorial(n):
    if n > 12 or n < 0: raise ValueError
    
    return math.factorial(n)

def factorial_refactored(n):
    if n < 0 or n > 12:
        raise ValueError
    return 1 if n <= 1 else n*factorial_refactored(n-1)
