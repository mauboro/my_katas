def points(games):
    total = 0
    for game in games:
        if int(game[0]) == int(game[-1]):
            total += 1
        elif int(game[0]) > int(game[-1]):
            total += 3
        elif int(game[0]) < int(game[-1]):
            pass
       
    return total
    
