def list_animals(animals):
    listy = "" 
    for i in range(len(animals)):
        listy += str(str(i + 1) + '. ' + animals[i] + '\n')
    return listy
