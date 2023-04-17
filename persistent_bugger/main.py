from math import prod

def persistence(number):
    times = 0
    res = number
    while len(str(res)) != 1:
        res = prod([int(n) for n in str(number)])
        number = res
        times += 1
    return times

def persistence_refactored(n):
    times = 0
    #while n >= 10 or
    while not(n < 10):
        n = eval("*".join([x for x in str(n)]))
        times += 1
    return times



