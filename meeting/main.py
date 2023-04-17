def meeting(s):
    res = sorted([(c.split(":")[1].upper(), c.split(":")[0].upper()) for c in s.split(";")])
    res = "".join([f'{r}' for r in res]).replace("'", "")
    return res
    
