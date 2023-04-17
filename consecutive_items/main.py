def consecutive(arr, a, b):
    for i, n in enumerate(arr):
        if n == a or n == b:
            try:
                if arr[i+1] == a or arr[i+1] == b:
                    return True
            except IndexError:
                return False
    return False
        
def consecutive_refactored(arr, a, b):
    return abs(arr.index(a) - arr.index(b)) == 1
