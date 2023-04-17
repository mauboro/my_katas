def calc_ms(n):
    res = 1
    for i in range(n):
        res *= 20
    return res


def calc_ms_refactored(n):
    return 20 ** n
