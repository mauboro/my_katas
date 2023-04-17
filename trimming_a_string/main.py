def trim(phrase, size):
    if len(phrase) <= 3:
        if len(phrase) > size:
            return phrase[:size] + "..."
        else:
            return phrase
    elif len(phrase) <= size:
        return phrase
    elif len(phrase) > size:
        if size <= 3:
            return phrase[:size] + "..."
        else:
            return phrase[:size-3] + "..."
    

