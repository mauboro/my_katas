def flatten(lst):
    res = []
    for l in lst:
        if type(l) == list:
            for i in l:
                res.append(i)
        else:
            res.append(l)
    return res
def flatten(lst):
    res = []
    for l in lst:
        if type(l) == list:
            res.extend(l)
        else:
            res.append(l)
    return res
