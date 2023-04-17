def remove(s, n):
    return "".join(s.split("!", n))

def remove_refactored(s, n):
    return s.replace("!", "", n)
