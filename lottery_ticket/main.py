def bingo(ticket,win):
    res = 0
    for part in ticket:
        for p in part[0]:
            if ord(p) == part[1]:
                res+=1
    return "Winner!" if res >= win else "Loser!"
