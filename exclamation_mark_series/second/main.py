def remove(s):
    points = 0
    for w in s[::-1]:
        if w == "!":
            points += 1
        elif w != "!":
            break
    s = s[::-1]
    s = s[points:]
    return s[::-1]
    
def remove_OBVIOUSLY_FUCKING_REFACTORED_YOU_MONKEY_MOVO(s):
    return s.rstrip("!")
            
