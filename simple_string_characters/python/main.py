from string import ascii_letters as letters

def solve(string):
    upper = len([s for s in string if s.isupper()])
    lower = len([s for s in string if s.islower()])
    numbers = len([s for s in string if s.isdigit()])
    ls_and_ns = letters + "0123456789"
    special = len([s for s in string if s not in ls_and_ns])
    return [upper, lower, numbers, special]

def solve_refactored(s):
    up, lo, n, sp = 0, 0, 0, 0
    for c in s:
        if c.isupper(): 
            up += 1
        elif c.islower(): 
            lo += 1
        elif c.isdigit(): 
            n += 1
        else:
            sp += 1
    return [up, lo, n, sp]

