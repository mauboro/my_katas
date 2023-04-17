def largest_pair_sum(numbers): 
    numbers.sort()
    return numbers[-1] + numbers[-2]

def largest_pair_sum_refactored(numbers):
    return sum(sorted(numbers)[-2:])
