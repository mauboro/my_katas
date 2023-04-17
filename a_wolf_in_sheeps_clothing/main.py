def warn_the_sheep(queue):
    if queue[-1] == "wolf":
        return "Pls go away and stop eating my sheep"
    for i, a in enumerate(queue):
        if a == "wolf":
            return f"Oi! Sheep number {len(queue) - (i + 1)}! You are about to be eaten by a wolf!"
            
