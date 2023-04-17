def remove_smallest(numberss):
    numbers = numberss.copy()
    for n in numbers:
        if n == min(numbers):
            numbers.remove(n)
            break
    return numbers


def remove_smallest_refactored(numbers):
    copy = numbers[:]
    if copy:
        copy.remove(min(copy))
    
    return copy
