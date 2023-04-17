def find_longest(arr):
    return int(max([str(a) for a in arr], key=len))
