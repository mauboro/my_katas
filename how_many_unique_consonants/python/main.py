def count_consonants(text):
    res = [t.lower() for t in text if t.lower() in "bcdfghjklmnpqrstvwxyz"]
    return len(set(res))
