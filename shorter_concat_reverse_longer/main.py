def shorter_reverse_longer(a,b):
    if len(a) >= len(b): 
        return b + a[::-1] + b
    else:
        return a + b[::-1] + a

def shorter_reverse_longer_refactored(a, b):
    if len(a) < len(b): a, b = b, a
    return b + a[::-1] + b

