def remove_rotten(bag):
    if not bag: return []
    return [fruit.replace("rotten", "").lower() for fruit in bag]
