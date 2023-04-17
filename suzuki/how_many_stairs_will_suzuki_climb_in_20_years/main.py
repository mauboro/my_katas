def stairs_in_20(stairs):
    total = 0
    for day in stairs:
        for d in day:
            total += d
    return total * 20

def stairs_in_20_refactored(stairs):
    return sum(sum(day) for day in stairs) * 20
