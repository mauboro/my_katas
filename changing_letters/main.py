def swap(st):
    return "".join([s.upper() if s in "aeiou" else s for s in st])
