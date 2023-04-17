def divisible_by(numbers, d):
    res = []
    for n in numbers:
        if not n % d:
            res.append(n)
    return res
