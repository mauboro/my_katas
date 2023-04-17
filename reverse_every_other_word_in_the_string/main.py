def reverse_alternate(s):
    return " ".join([c[::-1] if i % 2 else c for i, c in enumerate(s.split())])
