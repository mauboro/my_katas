def string_transformer(s):
    res = []
    temp = ""
    s = s.swapcase()
    for l in s:
        if l != " ":
            temp+=l
        elif l == " ":
            if temp: 
                res.append(temp)
                temp = ""
            res.append(" ")
    res.append(temp)
    return "".join(res[::-1])

def string_transformer_refactored(s):
    return ' '.join(s.swapcase().split(' ')[::-1])
