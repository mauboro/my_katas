def count_developers(lst):
    res = 0
    for l in lst:
        if "JavaScript" == l["language"] and "Europe" == l["continent"]:
            res+=1
    return res
