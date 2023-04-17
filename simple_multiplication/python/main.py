def simple_multiplication(n) :
    return n * 8 if n % 2 == 0 else n * 9

def simple_multiplication_kinda_refactored(n) :
    return n * (8 + n%2)
