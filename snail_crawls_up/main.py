def snail(column, day, night):
    total = day
    days = 1
    while total < column:
        total += day
        total -= night
        days += 1
   
    return days
    
