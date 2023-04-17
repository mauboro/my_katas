def sum_mul(n, m):
    total = 0
    if n == 0 or m == 0: return "INVALID"
    if n < 0 or m < 0: return "INVALID"

    for i in range(m):
        if i % n  == 0:
            total += i 
    return total
