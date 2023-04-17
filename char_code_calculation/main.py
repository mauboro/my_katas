def calc(x):
    total1 = "".join([str(ord(n)) for n in x])
    total2 = total1.replace("7", "1")
    total1 = sum(int(c) for c in total1)
    total2 = sum(int(c) for c in total2)
    return total1 - total2
    
