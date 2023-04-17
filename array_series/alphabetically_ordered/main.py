def alphabetic(s):
    return sorted([ord(l) for l in s]) == ([ord(l) for l in s])

def alphabetic(s):
    return sorted(s) == list(s)
