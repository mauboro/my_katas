def vowel_indices(word):
    res = []
    for i, l in enumerate(word):
        if l.lower() in "aeiouy":
            res.append(i + 1)
    return res

def vowel_indices_refactored(word):
    return [i for i, l in enumerate(word, 1) if l.lower() in "aeiouy"]
