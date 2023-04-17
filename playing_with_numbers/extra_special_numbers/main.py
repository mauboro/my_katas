def extra_perfect(number):
    res = []
    for n in range(number + 1):
        if bin(n)[2] == "1" and bin(n)[-1] == "1":
            res.append(n)
    return res

def extra_perfect_refactored(n):
    return list(range(1, n + 1, 2))
            


