def is_perfect(n):
    total = 1
    for i in range(2, n):
        if (i*i > n):
            break
        if n % i == 0:
            if i * i != n:
                total = total + i + n/i
            else:
                total += i
    if total == n and n != 1:
        return True
    return False
