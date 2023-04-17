def add(*args):
    total = 0
    for i, a in enumerate(args, 1):
        total += a / i
    return round(total)
