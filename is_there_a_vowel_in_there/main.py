def is_vow(inp):
    vowels = [ord(v) for v in "aeiou"]
    return [chr(n) if n in vowels else n for n in inp]


