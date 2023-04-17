def minimum_steps(numbers, value):
    total = 0
    times = 0
    while total < value:
        total += min(numbers)
        numbers.remove(min(numbers))
        times += 1
    times -=1
    return times
    
