def vowel_2_index(string):
    res = [str(i) if c.lower() in "aeiou" else c for i, c in enumerate(string, 1)]
    return "".join(res)
