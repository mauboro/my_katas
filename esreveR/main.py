def reverse(lst):
    res = list()
    for i in range(len(lst)-1, -1, -1):
        res.append(lst[i])
    return res

