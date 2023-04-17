def divisible_by_three(st): 
    n =  sum([int(c) for c in st])
    while n != 0:
        n -= 3
        if n < 0:
            return False
    return True
