def min_value(digits):
    return int("".join([str(n) for n in sorted(set(digits))]))

