def insert_dash(num):
    num = str(num)
    res = ""
    for i in range(len(num)):
        if int(num[i]) % 2 and int(num[i - 1]) % 2:
            res += "-"
            res += num[i]
        else: 
            res += num[i]
    return res.strip("-")
    
