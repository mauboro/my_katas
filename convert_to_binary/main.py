def to_binary(n):
    return int(bin(n)[2:])

def to_binary_refactored(n):
    #your code here
    return int(f"{n:b}")
