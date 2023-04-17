from string import ascii_lowercase as s 

def is_uppercase(inp):
    return True if len([c for c in s if c in inp]) == 0 else False

def is_uppercase_obviously_refactored_you_stupid_dumb_fuck_lol(inp):
    return inp.upper() == inp
