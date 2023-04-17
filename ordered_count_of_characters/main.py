def ordered_count(inp):
    pairs = {}
    for c in inp:
        if c not in pairs:
            pairs.update({c: inp.count(c)})
    
    return [(key, value) for key, value in pairs.items()]
    


def ordered_count_refactored_with_counter(inp):
    from collections import Counter

    return list(Counter(inp).items())

