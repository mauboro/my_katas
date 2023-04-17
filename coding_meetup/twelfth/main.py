def find_admin(lst, lang): 
    res = []
    for l in lst:
        if l["language"] == lang and "yes" in l["githubAdmin"]:
            res.append(l)
    return res0
