def pairs(ar):
    count = 0
    for i in range(0, len(ar), 2):
        if i + 1 == len(ar): break
        if ar[i] + 1 == ar[i + 1] or ar[i] - 1 == ar[i + 1]:
            count+=1
    return count
        
