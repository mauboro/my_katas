def growing_plant(up, down, desiredHeight):
    total = 0
    days = 0
    while total < desiredHeight:
        total += up
        if total >= desiredHeight:
            days += 1
            break
        total -= down
        days += 1
    return days
      
