def merge_arrays(arr1, arr2):
    arr1.extend(arr2)
    return sorted((set(arr1)))

def merge_arrays_refactored(arr1, arr2):
    return sorted((set(arr1 + arr2)))

