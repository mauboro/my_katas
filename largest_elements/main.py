def largest(n,xs):
    res = []
    for i in range(n):
        res.append(max(xs))
        xs.remove(max(xs))
    
    return res[::-1]

def largest_refactored(n,xs):
    return sorted(xs)[-n:]
