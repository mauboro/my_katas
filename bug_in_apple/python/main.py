def sc(apple):
    res = []
    for i, a in enumerate(apple):
        if "B" in a:
            res.append(i)
            res.append(a.index("B"))
            break
    return res
