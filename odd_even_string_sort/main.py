def sort_my_string(s):
    odds = "".join([c for i, c in enumerate(s) if i % 2])
    evens = "".join([c for i, c in enumerate(s) if i % 2 == 0])
    return "".join([evens, odds])

