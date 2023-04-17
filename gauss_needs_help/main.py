def f(n):
    print(n)
    if type(n) != int: return 
    if n <= 0: return 
    return sum(range(n + 1))
