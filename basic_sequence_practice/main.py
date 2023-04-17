def sum_of_n(n):
    count = [1]
    res = [0]
    if n > 0:
        for i in range(n):
            res.append(sum(count))
            count.append(count[-1] + 1)
    elif n < 0:
        for i in range(0, n, -1):
            res.append(sum(count) * -1)
            count.append((count[-1] + 1))
    return res
