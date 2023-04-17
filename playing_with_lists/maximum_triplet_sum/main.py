def max_tri_sum(numbers):
    return sum(sorted(list(set(numbers)))[-3:])
