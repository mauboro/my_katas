def split_in_parts(s, p): 
    res = ""
    for i, c in enumerate(s):
        if not i % p:
            res+=" "
        res+=c
    return res[1:]
