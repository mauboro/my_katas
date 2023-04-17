def switcheroo(s):
    return ''.join(["a" if c == "b" else "b" if c == "a" else c for c in s])

def switcheroo_refactored(s):
    return s.translate(str.maketrans("ab", "ba"))
