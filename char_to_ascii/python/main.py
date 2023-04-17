from string import ascii_letters as letters

def char_to_ascii(s):
    res = {}
    for c in s:
        if c in letters and s not in res:
            res.update({c: ord(c)})
    return res if res else None
    
