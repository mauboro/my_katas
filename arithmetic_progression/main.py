def arithmetic_sequence_elements(a, d, n):
    diff = d
    res = [a]
    for i in range(n-1):
        res.append(a+diff)
        diff += d
    return ", ".join([str(n) for n in res])
