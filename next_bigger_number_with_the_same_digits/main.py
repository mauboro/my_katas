def next_bigger(n):
    count = 0
    for i in range(n+1, n + 100000):
        comp = list(str(i))
        a = str(i)
        for c in str(n):
            if str(c) in comp:
                comp.remove(str(c))
        if len(comp) == 0: 
            return int(a) 
    return -1
