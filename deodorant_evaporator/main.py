def evaporator(content, evap_per_day, threshold):
    day = 0
    threshold = content * (threshold / 100)
    while content > threshold:
        content -= content * (evap_per_day / 100)
        day += 1
        
    return day
        
