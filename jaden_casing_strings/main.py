import string

def to_jaden_case(string):
    return ' '.join([c.capitalize() for c in string.split(" ")])

to_jaden_case_refactored = string.capwords


