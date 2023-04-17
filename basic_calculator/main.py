def calculate(n1, op, n2): 
    if op in "+-*/":
        try:
            return eval(f"{n1} {op} {n2}")
        except ZeroDivisionError:
            return None
    else:
        return None
