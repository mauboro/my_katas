import re
from string import ascii_lowercase as alphabet 

def solve(string):
    string = string.replace("a", " ")
    string = string.replace("e", " ")
    string = string.replace("i", " ")
    string = string.replace("o", " ")
    string = string.replace("u", " ")
    pairs = dict() 
    for word in string.split():
        pairs.update({word: sum([(alphabet.index(l) + 1) for l in word])})

    return max(pairs.values())

def solve_refactored_with_fucking_regex(string):
    return max(sum(ord(c)-96 for c in subs) for subs in re.split("[aeiou]+", string))

