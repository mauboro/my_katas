def even_numbers_before_fixed(sequence, fixed_element):
    count = 0
    if not fixed_element in sequence:
        return -1
    for n in sequence:
        if n == fixed_element:
            break
        elif n % 2 == 0:
            count += 1
    return count
