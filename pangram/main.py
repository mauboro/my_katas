from string import ascii_lowercase as letters

def is_pangram(s):
    letters_list = [c for c in letters]
    for l in s.lower():
        if l in letters_list:
            letters_list.remove(l)
    
    return len(letters_list) == 0

def is_pangram_refactored(s):
    for c in letters:
        if c not in s.lower():
            return False
    return True

def is_pangram_refactored_again(s):
    return set(letters).issubset(set(s.lower()))
