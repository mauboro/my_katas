def min_min_max(arr):
    mn = min(arr)
    mx = max(arr)
    mna = 0
    for i in range(mn, mx):
        if i not in arr:
            mna = i
            break
    return [mn, mna, mx]
    
