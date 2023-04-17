def last_survivor(letters, coords): 
    letters = [c for c in letters]
    for n in coords:
        letters.pop(n)
    return "".join(letters)
