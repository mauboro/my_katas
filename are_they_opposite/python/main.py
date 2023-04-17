def is_opposite(s1,s2):
    if not s1 or not s2: 
        return False
    return all([True if s1[i] != s2[i] and s1.lower() == s2.lower() else False for i in range(len(s1))] )

def is_opposite_refactored(s1, s2):
    return False if not (s1 or s2) else s1.swapcase() == s2
