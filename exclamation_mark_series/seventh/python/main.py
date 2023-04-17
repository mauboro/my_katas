def remove(s):
    res = []
    for w in s.split():
        if w.count("!") != 1:
            res.append(w)
    return " ".join(res)
