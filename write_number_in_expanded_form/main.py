def expanded_form(num):
    num = (str(num))
    total = []
    for i, n in enumerate(num[::-1]):
        if n != "0":
            total.append(str(n) + (i * "0"))
            
    return " + ".join(total[::-1])
            
