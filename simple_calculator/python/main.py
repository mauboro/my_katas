def calculator(x,y,op):
    if str(op) in "+/*-" and str(x) in "0123456789" and str(y) in "0123456789":
        return eval(f"{x} {op} {y}")
    else: 
        return "unknown value"
        
