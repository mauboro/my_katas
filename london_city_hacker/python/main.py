def london_city_hacker(journey): 
    res = 0
    count = 0
    for i in journey:
        if type(i) == str:
            res += 2.4
            count = 0
        elif type(i) == int:
            res += 1.5
            count += 1
        if count == 2:
            res -= 1.5
            count = 0
    if res == 0:
        return "£0.00"
    return "£" + str(round(res, 2)) + "0"
            
