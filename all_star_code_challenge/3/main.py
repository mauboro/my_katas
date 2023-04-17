def remove_vowels(string):
    return "".join([c if c not in "aeiou" else "" for c in string])
