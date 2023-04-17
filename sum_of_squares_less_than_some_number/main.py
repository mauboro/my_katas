def get_number_of_squares(n):
    total = 0
    inc = 1
    count = 0
    while total < n: 
        total += inc ** 2
        inc += 1
        count += 1
    return count - 1
        
