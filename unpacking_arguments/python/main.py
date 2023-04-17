from functools import reduce

def spread(func, args):
    temp =  reduce(func, args)
    if len(str(temp)) > 2:
        res = [] 
        for n in temp:
            if type(n) == tuple:
                for i in n:
                    res.append(i)
            else:
                res.append(n)
        return tuple(res)
    else:
        
        return temp
#congrats, dumbshit
def spred_refactored(func, args):
    return func(*args)
