def series_sum(n):
    if n == 0: return "0.00"
    total = 1.00
    div = 4
    for i in range(n - 1):
        total +=  1 / div
        div += 3
    return str(round(total, 2)).ljust(4, "0")
