def explode(string):
    return "".join([s * int(s) for s in string])
