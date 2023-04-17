import re

def decipher_this(string):
    n_res = [chr(int(s)) for s in re.findall(f"\d+", string)]
    res = []
    for i, s in enumerate(string.split()):
        res.append(s.replace(str(ord(n_res[i])), n_res[i]))
    res = " ".join(res)
    res = " ".join([s[0] + s[-1] + s[2:-1] + s[1] if len(s) > 2 else s for s in res.split()])
    
    return res
