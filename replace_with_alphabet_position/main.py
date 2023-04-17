from string import ascii_lowercase as s

def alphabet_position(text):
    result = []
    for l in text:
        if l.lower() in s:
            result.append(str(s.index(l.lower()) + 1))
    
    return " ".join(result)
