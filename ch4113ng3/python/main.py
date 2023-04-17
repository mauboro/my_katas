def nerdify(txt):
    res = ""
    for i in txt:
        if i.lower() == "a":
            res += ("4")
        elif i.lower() == "e":
            res += ("3")
        elif i == "l":
            res += ("1")
        else:
            res += (i)
    return res

def nerdify_refactored(txt):
    return txt.translate(str.maketrans("aAeEl", "44331"))
