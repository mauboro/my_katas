def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c.lower()) == 1 else ")" for c in word])
    
