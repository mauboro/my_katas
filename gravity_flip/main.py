def flip(d, a):
    if d == "R":
        return sorted(a)
    elif d == "L":
        return sorted(a, reverse=True)

def flib_refactored(d, a):
    return sorted(a, reverse=(d=="L"))

