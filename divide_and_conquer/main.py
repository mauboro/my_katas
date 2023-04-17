def div_con(x):
    return sum([n for n in x if isinstance(n, int)]) - sum([int(c) for c in x if isinstance(c, str)])
