def distinct(seq):
    unique_list = []
    seen = set()
    for x in seq:
        if x not in seen:
            unique_list.append(x)
            seen.add(x)
    return unique_list

def distinct_refactored(seq):
    return (sorted(set(seq), key = seq.index))


