def vowel_one(s):
    return "".join(["1" if c in "aeiouAEIOU" else "0" for c in s])
