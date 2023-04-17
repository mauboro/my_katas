def diamond(n):
    if n % 2 == 0 : return None
    diamond = []
    for i in range(n + 1):
        distance = (len(range(i, n, 2)))
        if i % 2 != 0:
            diamond.append(distance * " " + ("*" * i  + "\n"))
            
    for i in range(n, 0, -1)[1:]:
        distance = (len(range(i, n, 2)))
        if i % 2 != 0:
            diamond.append(distance * " " + ("*" * i  + "\n"))
        
    return "".join(diamond) if len(diamond) > 1 else None

