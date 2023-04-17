def power_of_two(x):
    for n in range(100):
        if 2 ** n  == x: 
            return True
    return False

def power_of_two_refactored(x):
    return bin(x).count("1") == 1
