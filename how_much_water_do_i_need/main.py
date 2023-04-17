def how_much_water(water, load, clothes):
    if load * 2 < clothes: return "Too much clothes"
    if load > clothes: return "Not enough clothes"
    return float(format((water * 1.1**(clothes-load)), ".2f"))

