def filter_string(string):
    return int("".join([n for n in string if n.isnumeric()]))
