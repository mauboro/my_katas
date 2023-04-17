def array_leaders(numbers):
    res = []
    for i, n in enumerate(numbers):
        if n > sum(numbers[i + 1:]):
            res.append(n)
    
    return res
