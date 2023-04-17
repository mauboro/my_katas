def mxdiflg(a1, a2):
    if len(a1) < 1 or len(a2) < 1:
        return -1
    
    a1 = [len(a) for a in a1]
    a2 = [len(a) for a in a2]
    
    res = []
    temp = []
    for n in a1:
        for i in range(len(a2)):
            temp.append(abs(n - a2[i]))
            
        res.append(max(temp))
        temp.clear()
    
    return max(res)

def mxdiflg_refactored(a1, a2):
    if a1 and a2:
        return max(
            len(max(a1, key=len)) - len(min(a2, key=len)),
            len(max(a2, key=len)) - len(min(a1, key=len)))
    return -1

