def digitize(n):
    return [int(c) for c in [c for c in str(n)][::-1]]
