def squares(x, n):
    if n <= 0 : return []
    current = x 
    res = [current]
    for _ in range(n - 1):
        res.append(current**2)
        current = current**2
    return res
