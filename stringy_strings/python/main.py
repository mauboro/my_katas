def stringy(size):
    res = ""
    shift = 1
    for i in range(size):
        if shift == 1:
            res += "1"
            shift = 0
        elif shift == 0:
            res += "0"
            shift = 1
    return res
