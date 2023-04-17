def replace_exclamation(s):
    return ''.join(["!" if c.lower() in "aeiou" else c for c in s])
