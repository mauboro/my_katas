def men_from_boys(arr):
    a = sorted([n for n in set(arr) if n % 2==0])
    b = sorted([n for n in set(arr) if n % 2], reverse=True)
    return a + b
