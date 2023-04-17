def multi_table(number):
    return "".join([f"{i + 1} * {number} = {number * (i + 1)}\n" for i in range(0, 10)])[:-1]

