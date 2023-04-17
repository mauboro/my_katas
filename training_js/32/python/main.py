import math

def round_it(n):
    string = (str(n).split("."))
    if len(string[0]) < len(string[1]):
        return math.ceil(n)
    elif len(string[0]) > len(string[1]):
        return math.floor(n)
    else:
        return round(n)
