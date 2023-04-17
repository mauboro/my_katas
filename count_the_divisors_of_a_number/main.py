def divisors(n):
    return sum([1 for d in range(1, n) if n % d == 0]) + 1
