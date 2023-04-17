def unique_in_order(iterable):
    if not iterable: return []
    temp = iterable[0]
    res = [iterable[0]]
    for i in iterable[1:]:
        if i == temp:
            temp = i
        elif i != temp:
            res.append(i)
            temp = i
    return res
