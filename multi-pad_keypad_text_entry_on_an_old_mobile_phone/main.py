def presses(phrase):
    dicto = {
        " 1*#ADGJMPTW": 1,
        "BEHKNQUX0": 2,
        "CFILORVY": 3,
        "234568SZ": 4,
        "79": 5
    }
    total = 0
    for c in phrase.upper():
        for key, value in dicto.items():
            if c in key:
                print(c, key, value)
                total += value
    return total 
