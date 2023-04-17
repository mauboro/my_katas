def xor(a,b):
    if a:
        if b: 
            return False
        if not b:
            return True
    if b:
        if a: 
            return False
        if not a:
            return True
   
    if not a and not b: 
        return False

#this uses regular brain use and common sense, things that I clearly don't have;
def xor_refactored(a, b):
    return a != b 

#this uses the bitwise xor operator
def xor_refactored_again(a, b):
    return a ^ b 

