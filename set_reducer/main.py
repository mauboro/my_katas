from itertools import groupby 

def set_reducer(inp):
    if len(inp) == 1:
        return inp[0]
    
    number = inp[0] 
    streak = 0
    res = []
    
    for n in inp:
        if n == number:
            streak += 1
        else:
            res.append(streak)
            number = n
            streak = 1 
            
    res.append(streak)
    
    return set_reducer(res)
          

def set_reducer_groupby(inp):
    return inp[0] if len(inp) == 1 else set_reducer([len([*g]) for n, g in groupby(inp)])

