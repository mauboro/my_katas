def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)

def sum_factorial(l):
    return sum(map(factorial, l))
