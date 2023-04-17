def cube_odd(arr):
    for n in arr:
        if type(n) != int:
            return None
    
    total = 0
    for n in [a**3 for a in arr if isinstance(a, int)]:
        if n % 2 != 0:
            total += n
    
    return total


def cube_odd_refactored(arr):
    return sum(n**3 for n in arr if n % 2) if all(type(n) == int for n in arr) else None
