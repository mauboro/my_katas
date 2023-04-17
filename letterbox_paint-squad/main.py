def paint_letterboxes(start, finish):
    res = []
    temp = 0 
    final = []
    for i in range(start, finish+1):
        res.append([int(c) for c in str(i)])
    for n in range(10):
        for r in res:
            temp += (r.count(n))
        final.append(temp)
        temp=0
    return final 
