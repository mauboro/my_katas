def outed(meet, boss):
    total = 0 
    for key, value in meet.items():
        if key == boss:
            total += value * 2 
        else:
            total += value
    total /= len(meet)
    return "Get Out Now!" if total <= 5 else "Nice Work Champ!"

def outed_refactored(meet, boss):
    if (sum(meet.values() + meet[boss]) / len(meet)) <= 5:
        return "Get Out Now!"
    else:
        return "Nice Work Champ!"
    
