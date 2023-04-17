def order(sentence):
    res = []
    for i, w in enumerate(sentence.split()):
        for s in sentence.split():
            if str(i) in s:
                res.append(s)
    for w in sentence.split():
        if w not in res:
            res.append(w)
    return " ".join(res)
