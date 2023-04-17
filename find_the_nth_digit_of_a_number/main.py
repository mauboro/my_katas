def find_digit(num, nth):
    if nth <= 0: return -1
    for i, n in enumerate(str(num)[::-1], 1):
        if str(i) == str(nth):
            return int(n)
    return 0
