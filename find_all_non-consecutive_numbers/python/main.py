def all_non_consecutive(arr):
    res = []
    for i in range(len(arr)):
        if arr[i] - arr[i - 1] != 1:
            res.append({"i": i, "n": arr[i]})
    return res[1:]
        
