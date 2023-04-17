def difference_of_squares(n):
    return abs(sum(n for n in range(1, n+1))**2 - sum(n**2 for n in range(1, n+1)))
        
