def sum_triangular_numbers(n):
    total = 0
    for i in range(n + 1):
        total += (i * (i + 1)) / 2
    
    return total
        
