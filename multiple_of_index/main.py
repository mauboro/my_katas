def multiple_of_index(arr):
    return [n for i, n in enumerate(arr[1:]) if n % (i + 1) == 0]

