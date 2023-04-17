def correct(s):
    result = []
    for c in s:
        if c == "0":
            result.append("O")
        elif c == "1":
            result.append("I")
        elif c == "5":
            result.append("S")
        else:
            result.append(c)
    
    return "".join(result)

def correct_refactored(s):
    return s.translate(str.maketrans("501", "SOI"))
