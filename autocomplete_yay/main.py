from string import ascii_lowercase

def autocomplete(inp, dicto):
    inp = "".join([l for l in inp if l.lower() in ascii_lowercase])
    res = []
    for w in dicto:
        if inp.lower() == w[:len(inp)].lower():
            res.append(w)
    return res[:5]
        
