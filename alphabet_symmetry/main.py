def solve(arr):
    total = 0
    l = []
    for a in arr:
        total = 0
        for i, n in enumerate(a, 1):
            if i == ord(n.lower()) - 96:
                total += 1
        l.append(total)
   
    return l
