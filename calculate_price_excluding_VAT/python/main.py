def excluding_vat_price(price):
    if not price:
        return - 1
    return round(price / (1 + 0.15), 2)
