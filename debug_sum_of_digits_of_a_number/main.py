def get_sum_of_digits(num):
    sum = 0
    for x in list(str(num)):
        sum += int(x)
    return sum

def get_sum_of_digits_refactored(num):
    return sum(map(int, str(num)))
