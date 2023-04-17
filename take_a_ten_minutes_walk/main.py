def is_valid_walk(walk):
    x = 0
    y = 0
    values = dict(n=1, s=-1, e=1, w=-1)
    if len(walk) == 10:
        for d in walk:
            if d == "n" or d == "s":
                x += values[d]
            elif d == "e" or d == "w":
                y += values[d]
        if (x, y) == (0, 0):
            return True
        else:
            return False
    else:
        return False
       

def is_valid_walk_refactored(walk):
    return len(walk) == 10 and walk.count("n") == walk.count("s") and walk.count("e") == walk.count("w")
