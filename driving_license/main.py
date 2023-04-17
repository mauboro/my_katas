def driver(data):
    dicto = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep":  "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }
    first = data[2][:5].upper().ljust(5, "9") 
    second = data[3].split("-")[2][2]
    if data[-1] == "F":
        day = data[-2].split("-")[0] 
        month = dicto[data[-2].split("-")[1][:3]] 
        third = str((50 + int(month))) + day
    elif data[-1] == "M":
        day = data[-2].split("-")[0] 
        month = dicto[data[-2].split("-")[1][:3]] 
        third = month + day
    fourth = data[-2].split("-")[-1][-1]
    fifth = data[0][0] + data[1][0] if data[1] else data[0][0] + "9"
    return (first + second + third + fourth + fifth + "9AA")
