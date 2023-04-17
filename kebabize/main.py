def kebabize(string):
    string = "".join([c for c in string if not c.isdigit() ])
    res = "".join([" " + c.lower() if c.isupper() else c.lower() for c in string]).strip()
    return res.replace(" ", "-")
    

