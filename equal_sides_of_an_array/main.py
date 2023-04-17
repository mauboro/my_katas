def find_even_index(arr):
    for i, n in enumerate(arr):
        if sum(arr[:i]) - sum(arr[i+1:]) == 0:
            return i
    return -1
