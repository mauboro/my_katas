def is_nice(arr):
    count = 0 
    for i in arr:
        for n in arr:
            if i == n + 1 or i == n - 1:
                count+=1
                break
    return count == len(arr) if len(arr) != 0 else False

def is_nice_refactored(arr):
    s = set(arr)
    return bool(s) and all(n + 1 in s or n - 1 in s for n in s)

def is_nice_refactored_again(arr):
    for x in arr:
        if x - 1 not in arr or x + 1 not in arr:
            return False
    return bool(1) and len(arr) > 0

