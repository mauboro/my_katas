def open_or_senior(data):
    res = []
    for pair in data:
        if pair[0] >= 55 and pair[1] > 7:
            res.append("Senior")
        else:
            res.append("Open")
    
    return res
