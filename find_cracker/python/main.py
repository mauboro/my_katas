def find_hack(arr):
    res = []
    grades = {"A": 30, "B": 20, "C": 10, "D": 5}
    for a in arr:
        if a[1] > 200:
            res.append(a[0])
            continue
        points = sum([grades.get(p, 0) for p in a[2]]) 
        if all([True if x == "A" or x == "B" else False for x in a[2]]) and len(a[2]) >= 5:
            if points + 20 <= 200:
                points += 20
            elif points + 20 > 200:
                points = 200
        if points > 200:
            points = 200
        if points != a[1]:
            res.append(a[0])
    return res
