def one(sq, fun): 
    return True if len([fun(i) for i in sq if fun(i)]) == 1 else False

def one_refactored(sq, fun):
    return sum(map(fun, sq)) == 1
