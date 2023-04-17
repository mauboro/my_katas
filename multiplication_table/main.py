def multiplication_table(size):
    res = []
    for i in range(1, size + 1):
        res.append([i * n for n in range(1, size + 1)])
    return res
