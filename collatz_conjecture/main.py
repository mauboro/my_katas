def hotpo(n):
    times = 0
    while n != 1:
        if n % 2:
            n = n*3 + 1
            times+=1
        elif n % 2 == 0:
            n = n / 2
            times+=1
    
    return times
