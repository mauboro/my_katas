def small_enough(array, limit):
    return sum(1 if n <= limit else 0 for n in array) == len(array)

def small_enough_refactored(array, limit):
    return max(array) <= limit
