def diff(n1, n2=0):
    return abs(n1 - n2)

def sum_of_differences(arr):
    arr = sorted(arr)[::-1]
    res = 0
    for i in range(1, len(arr)):
        res += diff(arr[i - 1], arr[i])
    return res

def sum_of_differences_refactored(arr):
    return max(arr) - min(arr) if arr else 0
