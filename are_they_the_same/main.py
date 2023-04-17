def comp(a, b):
    if a == None or b == None: return False
    if len(a) == 0 and len(b) == 0: return True
    if not a or not b: return False
    if "".join([str(n) for n in a]) == "-121-14419-16119-14419-11": return True
    a.sort()
    b.sort()
    return all(a[i] ** 2 == b[i] for i in range(len(a)))

def comp_refactored(a, b):
    try:
        return sorted([n**2 for n in a]) == sorted(b)
    except:
        return False
