from string import ascii_lowercase as letters

def is_letter(s):
    return s.lower() in letters and len(s) == 1
