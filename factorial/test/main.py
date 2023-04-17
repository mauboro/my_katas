def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    print(f"called, n is {n}")
    return 1 if n <= 1 else n*factorial(n-1)


print(factorial(5))
