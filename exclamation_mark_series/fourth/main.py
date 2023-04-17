def remove(s):
    return "".join([c if c != "!" else "" for c in s]) + "!"

def remove_refactored(s):
    return s.replace("!", "") + "!"
