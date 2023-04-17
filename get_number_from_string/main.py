def get_number_from_string(string):
    return int("".join([str(n) for n in string if n.isnumeric()]))
