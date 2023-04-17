def number(bus_stops):
    total = 0
    for stop in bus_stops:
        total += stop[0]
        total -= stop[1]
    
    return total
