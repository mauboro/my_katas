boredom(staff):
    boredom = { 
        "accounts": 1, 
        "finance": 2,
        "canteen": 10,
        "regulation": 6,
        "change": 6,
        "trading": 6,
        "IS": 8,
        "retail": 5,
        "cleaning": 4,
        "pissing about": 25
    } 
    total = sum([boredom[v] for v in staff.values()])
    return "kill me now" if total <= 80 else "i can handle this" if total < 100 and total > 80 else "party time!!" if total >= 100 else 0
