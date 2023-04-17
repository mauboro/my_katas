def first_non_repeated(s):
    return [c for c in s if s.count(c) == 1][0] if [c for c in s if s.count(c) == 1] else None

def first_non_repeated(s):
    for i in s:
        if s.count(i) == 1:
            return i

