def initials(name):
    res = ""
    for w in name.split():
        if w != name.split()[-1]:
            res += w[0].upper()
            res += "."
        else:
            res += w.title()
    return res
