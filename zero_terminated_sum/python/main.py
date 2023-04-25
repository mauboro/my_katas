def largest_sum(string):
    ns = (list(n for n in string.split("0")))
    res = []
    temp = 0
    for s in ns:
        for c in s:
            temp += int(c)
        res.append(temp)
        temp = 0
    return max(res)

def largest_sum_refactored(string):
    return max(sum(map(int, x) for x in string.split("0")))
