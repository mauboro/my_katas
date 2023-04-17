def consecutive(arr):
    arr = sorted(arr)
    res = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            res += abs(arr[i] - arr[i - 1]) - 1
    return res

def consecutive_refactored(arr):
    return max(arr) - min(arr) + 1 - len(arr) if arr else 0
