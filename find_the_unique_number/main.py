def find_uniq(arr):
    first = arr[0]
    for n in arr[1:]:
        if first == n:
            return sum([i for i in arr if i != n])
        if first != n and first == arr[-1]:
            return n 
        else:
            return first


def find_uniq_refactored(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

