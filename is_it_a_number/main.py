def isDigit(s):
    try:
        if type(float(s.strip())) == float:
            return True
    except ValueError:
        return False
        
        
