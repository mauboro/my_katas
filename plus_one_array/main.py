def up_array(arr):
    arr = [str(a) for a in arr]
    if not arr: return None
    if not all([False if len(a) != 1 or int(a) < 0 else True for a in arr]): return None
    has_zero = 0
    if arr[0] == "0" and len(arr) > 1:
        has_zero = 1
    else: 
        pass
    arr =  [int(a) for a in (str(int("".join(arr)) + 1))]
    print(arr)
    if has_zero:
        arr.insert(0, 0)
    return arr

def up_array_refactored(a):
    if not a or any(not 0 <= x < 10 for x in a): return
    for i in range(1, len(a)+1):
        a[-i] = (a[-i] + 1) % 10
        if a[-i]: break
    else: a[:0] = [1]
    return a
