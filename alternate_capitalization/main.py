def capitalize(s):
    return ["".join([c.upper() if i == 0 or i % 2 == 0 else c.lower() for i, c in enumerate(s)]), "".join([c.upper() if i % 2 != 0 else c.lower() for i, c in enumerate(s)])]


def capitalize_refactored(s):
    s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
    return [s, s.swapcase()]
