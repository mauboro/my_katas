def partlist(arr):
    res = []
    for i in range(1, len(arr) + 1):
        res.append((" ".join(arr[:i]), " ".join(arr[i:])))
    return res[:-1]
        
