def tidyNumber(n):
    return all(map(lambda a, b: int(a) <= int(b), str(n),str(n)[1:]))
