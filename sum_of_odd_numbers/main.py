def get_row(n):
    count = 2
    pattern = 1
    res = [pattern]
    for i in range(n):
        pattern += count 
        count += 1
        res.append(pattern)
    return res[-1] - res[-2]

def row_sum_odd_numbers(n):
    return sum(list(range(1, get_row(n), 2)))

row_sum_odd_numbers(2)
