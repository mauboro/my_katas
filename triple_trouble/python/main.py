def triple_trouble(one, two, three):
    res = ""
    for i in range(len(three)):
        res += one[i]
        res += two[i]
        res += three[i]
    return res
