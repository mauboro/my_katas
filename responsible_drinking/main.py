def hydrate(drink_string): 
    drinks = [int(n) for n in drink_string if n.isdigit()]
    return f"{sum(drinks)} glasses of water" if sum(drinks) > 1 else "1 glass of water"
