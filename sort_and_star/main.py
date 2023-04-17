def two_sort(array):
    return "***".join([c for c in sorted(array)[0]])

def two_sort_refactored(array):
    return "***".join(min(array))
