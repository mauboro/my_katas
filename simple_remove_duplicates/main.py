def solve(arr): 
    res = []
    for n in arr[::-1]:
        if n not in res:
            res.append(n)
        else:
            pass
        
    return res[::-1]
            
    
