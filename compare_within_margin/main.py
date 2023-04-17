def close_compare(a, b, margin=0):
    return 0 if abs(a - b) <= margin else 1 if abs(a - b) >= margin and a > b else -1
