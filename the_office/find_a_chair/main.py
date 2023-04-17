def meeting(rooms, need):
    if need == 0: return "Game On"
    res = []
    rest = 0 
    total = 0
    for r in rooms:
        if sum(res) < need:
            rest = r[1] - len(r[0])
            for i in range(rest):
                if sum(res) + total >= need:
                    break
                total += 1
            res.append(total)
            total = 0
    return "Not enough!" if not res or sum(res) < need else res 
