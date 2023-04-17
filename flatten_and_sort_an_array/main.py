def flatten_and_sort(array):
    result = []
    for arr in array:
        for a in arr:
            result.append(a)
    return sorted(result)
