def solve(a, b):
    res = []
    for c in a:
        if c not in b:
            res.append(c)
    for c in b:
        if c not in a:
            res.append(c)
    return "".join(res)
