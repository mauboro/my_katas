def remainder(a,b):
    try:
        return a % b if a > b else b % a
    except ZeroDivisionError:
        return None 
