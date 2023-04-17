from string import ascii_letters as letters

def encode(s):
    return "".join(["1" if c in letters and letters.index(c) % 2 else "0" if c in letters else c for c in s])
