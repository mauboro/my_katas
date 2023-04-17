def mult_triangle_timed_out(n):
    res = []
    for i in range(n + 1):
        for a in range(1, i):
            res.append(a * i)
        for a in range(i, 0, -1):
            res.append(a * i)
    
    return [sum(res), sum(n for n in res if n % 2 == 0), sum(n for n in res if n % 2)]
                          
