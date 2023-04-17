def snail(snail_map):
    snail_move = []
    for s in snail_map[0]:
        snail_move.append(s)
    for s in snail_map[1:]:
        snail_move.append(s[-1])
    for s in snail_map[-1:0:-1]:
        for ls in s[-2::-1]:
            snail_move.append(ls)
    
    return snail_move

array = [[1,2,3], [8,9,4], [7,6,5]]
print(snail(array))
