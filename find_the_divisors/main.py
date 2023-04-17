def divisors(i):
    res = []
    for n in range(2, i):
        if i % n == 0:
            res.append(n)
    return res if res else f"{i} is prime"
